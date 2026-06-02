"""
Application Settings Configuration
NAM-WH HMI System

This module loads settings from environment variables (.env file) with fallback defaults.
Priority: Environment Variables > .env file > Hardcoded Defaults
"""
import os
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv

from src.utils.paths import (
    get_app_dir,
    get_assets_dir,
    get_config_dir,
    get_data_dir,
    get_i18n_dir,
)

# APP_DIR = install/deploy directory ที่ binary หรือ source รันอยู่จริง
# Resolution: NAM_APP_DIR env var → sys.executable parent (with data/ sentinel)
# → cwd → source root.  ดู src/utils/paths.py และ docs/nuitka-deployment-caveats.md
APP_DIR = get_app_dir()

# Load environment variables from .env file
# Priority: APP_DIR/.env (install dir / dist/) > source-root .env (dev fallback)
_APP_ENV = APP_DIR / ".env"
_SRC_ENV = Path(__file__).resolve().parent.parent / ".env"
ENV_FILE = _APP_ENV if _APP_ENV.exists() else _SRC_ENV
load_dotenv(ENV_FILE, override=True)

# Base paths
DATA_DIR = get_data_dir()
ASSETS_DIR = get_assets_dir()
CONFIG_DIR = get_config_dir()
LOGS_DIR = DATA_DIR / "logs"

# BASE_DIR — kept for backward compatibility; aliased to APP_DIR so any caller
# that still resolves "config/" relative to BASE_DIR lands in the install dir
# instead of the Nuitka cache.
BASE_DIR = APP_DIR

# =============================================================================
# Application Settings
# =============================================================================
APP_NAME = os.getenv("APP_NAME", "NAM-WH HMI")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
MODEL = os.getenv("MODEL", "NAM-WH")
APP_AUTHOR = "Adasoft"

# =============================================================================
# Database Settings
# =============================================================================
def _resolve_under_app_dir(value: str, default: Path) -> Path:
    """Resolve a path setting against APP_DIR when relative.

    .env files commonly set ``DATABASE_PATH=data/nam_wh.db`` as a relative
    path.  Resolving against cwd is fragile (any ``os.chdir`` or alternate
    launcher breaks it), so anchor relative values to APP_DIR — the install
    dir we resolved through ``paths.get_app_dir()``.
    """
    if not value:
        return default
    p = Path(value)
    return p if p.is_absolute() else (APP_DIR / p)


DATABASE_PATH = _resolve_under_app_dir(
    os.getenv("DATABASE_PATH", ""), DATA_DIR / "nam_wh.db"
)
DATABASE_BACKUP_DIR = _resolve_under_app_dir(
    os.getenv("DATABASE_BACKUP_DIR", ""), DATA_DIR / "backups"
)
DATABASE_ECHO = os.getenv("DATABASE_ECHO", "false").lower() == "true"
DATABASE_BACKUP_ENABLED = os.getenv("DATABASE_BACKUP_ENABLED", "true").lower() == "true"

# =============================================================================
# PLC Communication Settings (Modbus TCP)
# =============================================================================
# Connection
PLC_HOST = os.getenv("PLC_HOST", "192.168.0.2")
PLC_PORT = int(os.getenv("PLC_PORT", "502"))
PLC_TIMEOUT = float(os.getenv("PLC_TIMEOUT", "3.0"))
PLC_RETRY_COUNT = int(os.getenv("PLC_RETRY_COUNT", "3"))
PLC_RETRY_DELAY = float(os.getenv("PLC_RETRY_DELAY", "1.0"))

# Modbus Protocol
MODBUS_UNIT_ID = int(os.getenv("MODBUS_UNIT_ID", "1"))
# Unitronics string payloads are typically low-byte first per register.
MODBUS_BYTE_ORDER = os.getenv("MODBUS_BYTE_ORDER", "little")
MODBUS_WORD_ORDER = os.getenv("MODBUS_WORD_ORDER", "big")

# Communication Type A Settings (PM Designer V2)
COMM_TYPE = "A"
BASE_ADDRESS_MI = 1700  # MI1700 (3 words)
SCAN_TIME = 0.25  # seconds

# Address Ranges (Type A Protocol)
BIT_ADDRESS_START = 0  # $C0.0
BIT_ADDRESS_END = 2  # $C2.f
WORD_ADDRESS_START = 0  # $C0
WORD_ADDRESS_END = 2  # $C2

# Screen Switching
SCREEN_REGISTER = 0  # $C0
CURRENT_SCREEN_MI = 1700  # MI1700 - Current screen number

# Connection Health
HEALTH_CHECK_INTERVAL = float(os.getenv("HEALTH_CHECK_INTERVAL", "5.0"))
HEALTH_CHECK_REGISTER = 1700
MAX_CONSECUTIVE_FAILURES = int(os.getenv("MAX_CONSECUTIVE_FAILURES", "5"))
# Fallback backend when nmcli is unavailable
PI_NETWORK_INTERFACES_FILE = os.getenv("PI_NETWORK_INTERFACES_FILE", "/etc/network/interfaces")

# Optimization
ENABLE_BATCH_READ = os.getenv("ENABLE_BATCH_READ", "true").lower() == "true"
MAX_BATCH_SIZE = int(os.getenv("MAX_BATCH_SIZE", "100"))
ENABLE_CACHE = os.getenv("ENABLE_CACHE", "true").lower() == "true"
# Cache TTL ต้อง >= UI_UPDATE_INTERVAL (100ms) เพื่อให้ cache ยังใช้ได้ระหว่าง tick ถัดไป
# ค่า 250ms ทำให้ cache อยู่ได้หลาย tick และลด Modbus TCP requests อย่างมีนัยสำคัญ
CACHE_TTL = float(os.getenv("CACHE_TTL", "0.25"))  # 250ms (>= UI_UPDATE_INTERVAL 100ms)

# Stats & Monitoring
LOG_COMMUNICATION_STATS = os.getenv("LOG_COMMUNICATION_STATS", "true").lower() == "true"
STATS_LOG_INTERVAL = int(os.getenv("STATS_LOG_INTERVAL", "60"))

# =============================================================================
# UI Settings
# =============================================================================
UI_FRAMEWORK = os.getenv("UI_FRAMEWORK", "PySide6")
SCREEN_WIDTH = int(os.getenv("SCREEN_WIDTH", "1024"))
SCREEN_HEIGHT = int(os.getenv("SCREEN_HEIGHT", "600"))
DISPLAY_SCREEN_INDEX = int(os.getenv("DISPLAY_SCREEN_INDEX", "0"))
FULLSCREEN = os.getenv("FULLSCREEN", "true").lower() == "true"
HIDE_CURSOR = os.getenv("HIDE_CURSOR", "false").lower() == "true"
IDLE_SCREEN_BLANK_ENABLED = os.getenv("IDLE_SCREEN_BLANK_ENABLED", "false").lower() == "true"
IDLE_SCREEN_BLANK_TIMEOUT_SECONDS = int(
    os.getenv("IDLE_SCREEN_BLANK_TIMEOUT_SECONDS", "300")
)

# Second display (sub-screen) settings
SCREEN2_ENABLED       = os.getenv("SCREEN2_ENABLED", "false").lower() == "true"
SCREEN2_DISPLAY_INDEX = int(os.getenv("SCREEN2_DISPLAY_INDEX", "1"))
SCREEN2_WIDTH         = int(os.getenv("SCREEN2_WIDTH", "1024"))
SCREEN2_HEIGHT        = int(os.getenv("SCREEN2_HEIGHT", "600"))

# =============================================================================
# Language Settings
# =============================================================================
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "th_TH")

# =============================================================================
# Timezone Settings
# =============================================================================
APP_TIMEZONE = os.getenv("APP_TIMEZONE", "Asia/Bangkok")
SUPPORTED_LANGUAGES = os.getenv("SUPPORTED_LANGUAGES", "th_TH,en_GB").split(",")
TRANSLATION_DIR = get_i18n_dir()

# =============================================================================
# Session Settings
# =============================================================================
SESSION_TIMEOUT = int(os.getenv("SESSION_TIMEOUT", "900"))  # 15 minutes
AUTO_LOGOUT_ENABLED = os.getenv("AUTO_LOGOUT_ENABLED", "true").lower() == "true"
INACTIVITY_CHECK_INTERVAL = int(os.getenv("INACTIVITY_CHECK_INTERVAL", "60"))

# =============================================================================
# Logging Settings
# =============================================================================
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = _resolve_under_app_dir(os.getenv("LOG_FILE", ""), LOGS_DIR / "app.log")
LOG_MAX_BYTES = int(os.getenv("LOG_MAX_BYTES", str(10 * 1024 * 1024)))  # 10 MB
LOG_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", "5"))
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# =============================================================================
# Performance Settings (Polling Intervals)
# =============================================================================
PLC_POLLING_INTERVAL = float(os.getenv("PLC_POLLING_INTERVAL", "0.1"))  # 100ms
DATA_LOGGING_INTERVAL = int(os.getenv("DATA_LOGGING_INTERVAL", "5"))  # 5 seconds
ALARM_POLLING_INTERVAL = float(os.getenv("ALARM_POLLING_INTERVAL", "0.5"))  # 500ms
UI_UPDATE_INTERVAL = float(os.getenv("UI_UPDATE_INTERVAL", "0.1"))  # 100ms

# Screen 18 performance modes
# - "realtime":          sync basket names every worker tick (default, test sync with legacy panel)
# - "on_enter_after_save": refresh names only on screen enter + after save
S18_NAME_REFRESH_MODE = os.getenv("S18_NAME_REFRESH_MODE", "realtime").strip().lower()
# Position button UI refresh cadence for Screen 18 (UI-side throttle).
# Keep 100ms for strict sync; set 250-500ms to reduce style recalculation load.
S18_POS_UI_REFRESH_INTERVAL_MS = int(os.getenv("S18_POS_UI_REFRESH_INTERVAL_MS", "100"))

# Button Settings (Momentary ON behavior from PM Designer V2)
BUTTON_PULSE_WIDTH = float(os.getenv("BUTTON_PULSE_WIDTH", "0.05"))  # 50ms (Minimal Pulse Width)

# Reconnection Settings
RECONNECT_MAX_BACKOFF = float(os.getenv("RECONNECT_MAX_BACKOFF", "60.0"))  # Max 60 seconds
RECONNECT_ERROR_SLEEP = float(os.getenv("RECONNECT_ERROR_SLEEP", "1.0"))  # Sleep on error

# =============================================================================
# Data Format Settings (PM Designer V2 specifications)
# =============================================================================
# Program/Basket name: 10 words = 20 characters
PROGRAM_NAME_LENGTH = int(os.getenv("PROGRAM_NAME_LENGTH", "10"))  # words (registers)
BASKET_NAME_LENGTH = int(os.getenv("BASKET_NAME_LENGTH", "10"))  # words (registers)

# Screen configuration
MAX_SCREEN_NUMBER = int(os.getenv("MAX_SCREEN_NUMBER", "30"))  # Total screens in HMI

# Temperature validation range (°C)
TEMP_VALIDATION_MIN = int(os.getenv("TEMP_VALIDATION_MIN", "0"))
TEMP_VALIDATION_MAX = int(os.getenv("TEMP_VALIDATION_MAX", "200"))

# =============================================================================
# Security Settings
# =============================================================================
PASSWORD_MIN_LENGTH = int(os.getenv("PASSWORD_MIN_LENGTH", "4"))
PASSWORD_HASH_ALGORITHM = "bcrypt"
ENABLE_AUDIT_LOG = os.getenv("ENABLE_AUDIT_LOG", "true").lower() == "true"
# Permission enforcement (set false during testing to bypass all permission checks)
ENABLE_PERMISSION = os.getenv("ENABLE_PERMISSION", "true").lower() == "true"

# =============================================================================
# RFID Settings
# =============================================================================
RFID_ENABLED = os.getenv("RFID_ENABLED", "true").lower() == "true"
RFID_PORT = os.getenv("RFID_PORT", "/dev/ttyUSB0")
RFID_BAUD_RATE = int(os.getenv("RFID_BAUD_RATE", "9600"))
RFID_TIMEOUT = int(os.getenv("RFID_TIMEOUT", "5"))
RFID_AUTO_LOGOUT_ON_REMOVAL = os.getenv("RFID_AUTO_LOGOUT_ON_REMOVAL", "true").lower() == "true"

# =============================================================================
# Alarm Settings
# =============================================================================
ALARM_AUDIO_ENABLED = os.getenv("ALARM_AUDIO_ENABLED", "true").lower() == "true"
ALARM_CRITICAL_BEEPS = int(os.getenv("ALARM_CRITICAL_BEEPS", "3"))
ALARM_WARNING_BEEPS = int(os.getenv("ALARM_WARNING_BEEPS", "1"))
ALARM_WARNING_AUTO_DISMISS = int(os.getenv("ALARM_WARNING_AUTO_DISMISS", "10"))  # seconds

# =============================================================================
# Trend Logging Settings
# =============================================================================
# Buffer capacity: 7200 = 2 hours @ 1 sample/second (TrendSamplingService)
TREND_MAX_SAMPLES = int(os.getenv("TREND_MAX_SAMPLES", "7200"))

# =============================================================================
# Data Retention
# =============================================================================
TREND_DATA_RETENTION_DAYS = int(os.getenv("TREND_DATA_RETENTION_DAYS", "30"))
AUDIT_LOG_RETENTION_DAYS = int(os.getenv("AUDIT_LOG_RETENTION_DAYS", "90"))
ALARM_HISTORY_RETENTION_DAYS = int(os.getenv("ALARM_HISTORY_RETENTION_DAYS", "365"))

# =============================================================================
# IoT Integration (Optional - Phase 2/3)
# =============================================================================
IOT_ENABLED = os.getenv("IOT_ENABLED", "false").lower() == "true"
THINGSBOARD_HOST = os.getenv("THINGSBOARD_HOST", "thingsboard.cloud")
THINGSBOARD_PORT = int(os.getenv("THINGSBOARD_PORT", "1883"))
DEVICE_ACCESS_TOKEN = os.getenv("DEVICE_ACCESS_TOKEN", "")
TELEMETRY_INTERVAL = int(os.getenv("TELEMETRY_INTERVAL", "10"))

# =============================================================================
# Development/Testing Settings
# =============================================================================
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
MOCK_PLC = os.getenv("MOCK_PLC", "false").lower() == "true"
SHOW_DEBUG_INFO = os.getenv("SHOW_DEBUG_INFO", "false").lower() == "true"


# =============================================================================
# Helper Functions
# =============================================================================

def get_config() -> Dict[str, Any]:
    """
    Get configuration dictionary (commonly used settings)

    Returns:
        dict: Configuration settings
    """
    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "model": MODEL,
        "database_path": str(DATABASE_PATH),
        "ui_framework": UI_FRAMEWORK,
        "screen_size": (SCREEN_WIDTH, SCREEN_HEIGHT),
        "fullscreen": FULLSCREEN,
        "default_language": DEFAULT_LANGUAGE,
        "session_timeout": SESSION_TIMEOUT,
        "log_level": LOG_LEVEL,
        "plc_polling_interval": PLC_POLLING_INTERVAL,
        "debug_mode": DEBUG_MODE,
    }


def get_plc_config() -> Dict[str, Any]:
    """
    Get PLC configuration dictionary

    Returns:
        dict: PLC configuration
    """
    return {
        "host": PLC_HOST,
        "port": PLC_PORT,
        "timeout": PLC_TIMEOUT,
        "retry_count": PLC_RETRY_COUNT,
        "retry_delay": PLC_RETRY_DELAY,
        "unit_id": MODBUS_UNIT_ID,
        "byte_order": MODBUS_BYTE_ORDER,
        "word_order": MODBUS_WORD_ORDER,
        "scan_time": SCAN_TIME,
        "current_screen_mi": CURRENT_SCREEN_MI,
        "health_check_interval": HEALTH_CHECK_INTERVAL,
        "enable_batch_read": ENABLE_BATCH_READ,
        "enable_cache": ENABLE_CACHE,
    }


def create_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        DATA_DIR,
        LOGS_DIR,
        DATABASE_BACKUP_DIR,
        ASSETS_DIR,
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def validate_config():
    """
    Validate configuration settings and raise errors if invalid

    Raises:
        ValueError: If configuration is invalid
    """
    errors = []

    # Validate screen size
    if SCREEN_WIDTH < 800 or SCREEN_HEIGHT < 480:
        errors.append(f"Screen size too small: {SCREEN_WIDTH}x{SCREEN_HEIGHT} (minimum 800x480)")

    # Validate PLC settings
    if PLC_PORT < 1 or PLC_PORT > 65535:
        errors.append(f"Invalid PLC port: {PLC_PORT}")

    if PLC_TIMEOUT <= 0:
        errors.append(f"Invalid PLC timeout: {PLC_TIMEOUT}")

    # Validate intervals
    if PLC_POLLING_INTERVAL <= 0:
        errors.append(f"Invalid PLC polling interval: {PLC_POLLING_INTERVAL}")

    # Validate language
    if DEFAULT_LANGUAGE not in SUPPORTED_LANGUAGES:
        errors.append(f"Default language '{DEFAULT_LANGUAGE}' not in supported languages")

    if errors:
        raise ValueError("Configuration validation failed:\n" + "\n".join(f"  - {err}" for err in errors))


# Create directories and validate on import
create_directories()

# Only validate if not in test mode
if not os.getenv("PYTEST_CURRENT_TEST"):
    try:
        validate_config()
    except ValueError as e:
        print(f"WARNING: {e}")
