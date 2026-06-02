"""
Database Schema Documentation
Defines the database structure for NAM-WH HMI system
"""

# =============================================================================
# DATABASE SCHEMA OVERVIEW
# =============================================================================

"""
NAM-WH HMI Database Schema (SQLite)

Tables:
1. users - User accounts and authentication
2. roles - User roles and permissions
3. user_sessions - Active user sessions (login/logout tracking)
4. alarm_logs - Alarm history and acknowledgments
5. cycle_logs - Wash cycle history and statistics
6. audit_logs - System audit trail
7. system_settings - Application settings (key-value store)

Relationships:
- users.role_id -> roles.id (Many-to-One)
- user_sessions.user_id -> users.id (Many-to-One)
- alarm_logs.acknowledged_by -> users.id (Many-to-One, nullable)
- cycle_logs.user_id -> users.id (Many-to-One)
- audit_logs.user_id -> users.id (Many-to-One, nullable)
"""

# =============================================================================
# TABLE: users
# =============================================================================

"""
users - User accounts for HMI system

Columns:
- id (INTEGER, PK, AUTO_INCREMENT): User ID
- username (VARCHAR(50), UNIQUE, NOT NULL): Login username
- password_hash (VARCHAR(255), NOT NULL): Bcrypt password hash
- full_name (VARCHAR(100), NOT NULL): Full name (Thai/English)
- card_id (VARCHAR(50), UNIQUE, NULLABLE): RFID card ID
- role_id (INTEGER, FK->roles.id, NOT NULL): User role
- is_active (BOOLEAN, DEFAULT TRUE): Account active status
- language (VARCHAR(5), DEFAULT 'th_TH'): Preferred language (th_TH, en_GB)
- created_at (DATETIME, NOT NULL): Account creation timestamp
- updated_at (DATETIME, NOT NULL): Last update timestamp
- last_login (DATETIME, NULLABLE): Last successful login

Indexes:
- idx_users_username (username)
- idx_users_card_id (card_id)
- idx_users_role_id (role_id)

Constraints:
- username: 3-50 characters, alphanumeric + underscore
- password_hash: bcrypt format ($2b$...)
- card_id: 8-20 characters, hex format
- language: 'th_TH' or 'en_GB'

Default Users:
1. admin (username: 'admin', role: Administrator)
2. operator (username: 'operator', role: Operator)
3. maintenance (username: 'maintenance', role: Maintenance)
"""

# =============================================================================
# TABLE: roles
# =============================================================================

"""
roles - User roles and permission levels

Columns:
- id (INTEGER, PK, AUTO_INCREMENT): Role ID
- role_name (VARCHAR(50), UNIQUE, NOT NULL): Role name
- description (VARCHAR(255)): Role description
- permissions (TEXT, NOT NULL): JSON array of permission strings
- created_at (DATETIME, NOT NULL): Role creation timestamp

Permissions (JSON array):
- "view_home": View home screen
- "start_cycle": Start wash cycle
- "stop_cycle": Stop wash cycle
- "acknowledge_alarm": Acknowledge alarms
- "view_manual": View manual control screen
- "use_manual": Use manual control (maintenance only)
- "edit_programs": Edit program settings
- "edit_baskets": Edit basket configurations
- "view_users": View user list
- "edit_users": Create/edit/delete users
- "view_settings": View system settings
- "edit_settings": Edit system settings
- "view_alarms": View alarm history
- "view_cycles": View cycle history
- "view_trends": View trend data

Default Roles:
1. Administrator - Full access to all features
2. Operator - Basic operation (start/stop cycles, view data)
3. Maintenance - Operation + manual control + program editing
4. Viewer - Read-only access (no control)
"""

# =============================================================================
# TABLE: user_sessions
# =============================================================================

"""
user_sessions - User login/logout session tracking

Columns:
- id (INTEGER, PK, AUTO_INCREMENT): Session ID
- user_id (INTEGER, FK->users.id, NOT NULL): User ID
- login_method (VARCHAR(20), NOT NULL): Login method ('password', 'rfid')
- login_time (DATETIME, NOT NULL): Login timestamp
- logout_time (DATETIME, NULLABLE): Logout timestamp (NULL = still active)
- session_duration (INTEGER, NULLABLE): Duration in seconds
- ip_address (VARCHAR(45), NULLABLE): IP address (IPv4/IPv6)
- device_info (VARCHAR(100), NULLABLE): Device information

Indexes:
- idx_sessions_user_id (user_id)
- idx_sessions_login_time (login_time)
- idx_sessions_active (logout_time) - for active sessions

Business Rules:
- Only one active session per user allowed (logout previous session on new login)
- Auto-logout after 12 hours of inactivity
- Session duration calculated on logout
"""

# =============================================================================
# TABLE: alarm_logs
# =============================================================================

"""
alarm_logs - Alarm occurrence and acknowledgment history

Columns:
- id (INTEGER, PK, AUTO_INCREMENT): Log ID
- alarm_mb (INTEGER, NOT NULL): Alarm MB address (136-301)
- alarm_code (VARCHAR(10), NOT NULL): Alarm code (e.g., 'ALM-001')
- alarm_name (VARCHAR(100), NOT NULL): Alarm name
- alarm_level (INTEGER, NOT NULL): Alarm level (1=Warning, 2=Critical)
- alarm_message (TEXT, NOT NULL): Alarm message (Thai/English)
- occurred_at (DATETIME, NOT NULL): Alarm occurrence timestamp
- acknowledged (BOOLEAN, DEFAULT FALSE): Acknowledgment status
- acknowledged_at (DATETIME, NULLABLE): Acknowledgment timestamp
- acknowledged_by (INTEGER, FK->users.id, NULLABLE): User who acknowledged
- auto_cleared (BOOLEAN, DEFAULT FALSE): Auto-cleared (not acknowledged)
- cleared_at (DATETIME, NULLABLE): Clear timestamp
- duration (INTEGER, NULLABLE): Alarm duration in seconds
- plc_screen (INTEGER, NULLABLE): Screen number when alarm occurred
- cycle_log_id (INTEGER, FK->cycle_logs.id, NULLABLE): Associated cycle

Indexes:
- idx_alarm_logs_alarm_mb (alarm_mb)
- idx_alarm_logs_occurred_at (occurred_at)
- idx_alarm_logs_acknowledged (acknowledged)
- idx_alarm_logs_alarm_level (alarm_level)

Business Rules:
- Log created immediately when alarm goes active (MB=1)
- acknowledged=TRUE when user clicks Acknowledge button
- Auto-cleared warnings (Level 1) after 10 seconds if not acknowledged
- Critical alarms (Level 2) require explicit acknowledgment
"""

# =============================================================================
# TABLE: cycle_logs
# =============================================================================

"""
cycle_logs - Wash cycle history and statistics

Columns:
- id (INTEGER, PK, AUTO_INCREMENT): Cycle ID
- cycle_number (INTEGER, NOT NULL): Cycle counter (from MI1005)
- user_id (INTEGER, FK->users.id, NOT NULL): User who started cycle
- program_number (INTEGER, NOT NULL): Program number (1-6)
- program_name (VARCHAR(100), NOT NULL): Program name
- basket_number (INTEGER, NOT NULL): Basket number
- basket_name (VARCHAR(100), NOT NULL): Basket name
- start_time (DATETIME, NOT NULL): Cycle start timestamp
- end_time (DATETIME, NULLABLE): Cycle end timestamp (NULL = running)
- duration (INTEGER, NULLABLE): Actual duration in seconds
- expected_duration (INTEGER, NOT NULL): Expected duration in seconds
- status (VARCHAR(20), NOT NULL): Status (running, completed, stopped, aborted)
- stop_reason (VARCHAR(100), NULLABLE): Reason for stop (if stopped)
- step_count (INTEGER, NULLABLE): Number of steps completed
- water_usage (FLOAT, NULLABLE): Water usage in liters
- chemical1_usage (FLOAT, NULLABLE): Chemical 1 usage in ml
- chemical2_usage (FLOAT, NULLABLE): Chemical 2 usage in ml
- chemical3_usage (FLOAT, NULLABLE): Chemical 3 usage in ml
- max_chamber_temp (INTEGER, NULLABLE): Max chamber temperature (°C)
- max_dry_temp (INTEGER, NULLABLE): Max dry temperature (°C)
- alarm_count (INTEGER, DEFAULT 0): Number of alarms during cycle
- notes (TEXT, NULLABLE): Additional notes

Indexes:
- idx_cycle_logs_cycle_number (cycle_number)
- idx_cycle_logs_start_time (start_time)
- idx_cycle_logs_status (status)
- idx_cycle_logs_user_id (user_id)
- idx_cycle_logs_program_number (program_number)

Business Rules:
- Log created when cycle starts (Screen 8 -> Screen 9)
- Updated during cycle with real-time data
- Finalized when cycle completes (Screen 20)
- status='stopped' if user stops cycle manually
- status='aborted' if critical alarm forces stop
"""

# =============================================================================
# TABLE: audit_logs
# =============================================================================

"""
audit_logs - System audit trail for security and compliance

Columns:
- id (INTEGER, PK, AUTO_INCREMENT): Log ID
- timestamp (DATETIME, NOT NULL): Event timestamp
- user_id (INTEGER, FK->users.id, NULLABLE): User ID (NULL for system events)
- event_type (VARCHAR(50), NOT NULL): Event type
- event_category (VARCHAR(50), NOT NULL): Event category
- event_description (TEXT, NOT NULL): Event description
- screen_number (INTEGER, NULLABLE): Screen number where event occurred
- ip_address (VARCHAR(45), NULLABLE): IP address
- success (BOOLEAN, DEFAULT TRUE): Event success status
- error_message (TEXT, NULLABLE): Error message if failed
- old_value (TEXT, NULLABLE): Previous value (for changes)
- new_value (TEXT, NULLABLE): New value (for changes)
- metadata (TEXT, NULLABLE): Additional JSON metadata

Indexes:
- idx_audit_logs_timestamp (timestamp)
- idx_audit_logs_user_id (user_id)
- idx_audit_logs_event_type (event_type)
- idx_audit_logs_event_category (event_category)

Event Categories:
- 'authentication': Login, logout, failed login
- 'cycle': Cycle start, stop, complete
- 'alarm': Alarm acknowledge, alarm cleared
- 'configuration': Program edit, basket edit, settings change
- 'user_management': User create, edit, delete, role change
- 'system': Application start, stop, PLC connect/disconnect
- 'manual_control': Manual operation (pumps, valves, etc.)

Business Rules:
- All security-sensitive operations must be logged
- Configuration changes must log old and new values
- Failed operations must be logged with error messages
- Logs are write-only (no updates or deletes)
"""

# =============================================================================
# TABLE: system_settings
# =============================================================================

"""
system_settings - Application configuration (key-value store)

Columns:
- id (INTEGER, PK, AUTO_INCREMENT): Setting ID
- key (VARCHAR(100), UNIQUE, NOT NULL): Setting key
- value (TEXT, NOT NULL): Setting value (JSON or plain text)
- data_type (VARCHAR(20), NOT NULL): Data type (string, integer, boolean, json)
- category (VARCHAR(50), NOT NULL): Setting category
- description (VARCHAR(255)): Setting description
- is_editable (BOOLEAN, DEFAULT TRUE): User-editable flag
- updated_at (DATETIME, NOT NULL): Last update timestamp
- updated_by (INTEGER, FK->users.id, NULLABLE): User who updated

Indexes:
- idx_settings_key (key)
- idx_settings_category (category)

Setting Categories:
- 'plc': PLC connection settings
- 'ui': UI preferences
- 'alarm': Alarm system settings
- 'logging': Data logging settings
- 'iot': IoT gateway settings
- 'system': System-level settings

Example Settings:
- plc.host (string): "192.168.1.100"
- plc.port (integer): 502
- plc.polling_interval (integer): 100
- ui.default_language (string): "th_TH"
- ui.screen_timeout (integer): 300
- alarm.beep_enabled (boolean): true
- alarm.auto_dismiss_warnings (boolean): true
- alarm.warning_dismiss_delay (integer): 10
- logging.enabled (boolean): true
- logging.interval (integer): 5
- iot.enabled (boolean): false
- iot.server_url (string): "mqtt://thingsboard.cloud"
"""

# =============================================================================
# DATABASE PERFORMANCE CONSIDERATIONS
# =============================================================================

"""
Performance Optimizations:

1. Indexes:
   - All foreign keys indexed
   - Timestamp columns indexed for time-range queries
   - Status columns indexed for filtering
   - Unique constraints on username, card_id

2. Partitioning (Future):
   - alarm_logs: Partition by month (if > 1M records)
   - cycle_logs: Partition by month
   - audit_logs: Partition by month

3. Archiving Strategy:
   - Keep 3 months of data in main tables
   - Archive older data to separate tables
   - Provide archive query interface

4. Query Optimization:
   - Use prepared statements via SQLAlchemy
   - Batch inserts for bulk operations
   - Use transactions for multi-table operations
   - Lazy loading for relationships

5. Maintenance:
   - VACUUM database monthly
   - ANALYZE after bulk data changes
   - Backup database daily
   - Monitor database file size
"""

# =============================================================================
# MIGRATION STRATEGY
# =============================================================================

"""
Migration Approach:

1. Version Control:
   - Each schema change gets a version number
   - Version stored in system_settings (schema_version)
   - Migrations are idempotent (can run multiple times safely)

2. Migration Scripts:
   - scripts/db_migrations/001_initial_schema.sql
   - scripts/db_migrations/002_add_card_id_column.sql
   - scripts/db_migrations/003_add_cycle_statistics.sql

3. Rollback Support:
   - Each migration has a corresponding rollback script
   - Rollback scripts in scripts/db_migrations/rollback/

4. Data Migration:
   - Separate scripts for data transformations
   - Preserve historical data during schema changes
"""
