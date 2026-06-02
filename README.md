# NAM-WH HMI System

Medical/Industrial Washing Machine Human-Machine Interface (HMI) system built with Python and PySide6.

## Overview

This project replaces the traditional commercial HMI touchscreen panel with a **Raspberry Pi CM5** (Compute Module 5) based system running a Python application. The system communicates with the existing PLC via Modbus TCP protocol while providing enhanced features including:

- 30 touchscreen interface screens
- Multi-language support (Thai/English)
- RFID card reader authentication
- 44 alarm monitoring system
- Data logging and trend analysis
- IoT integration with ThingsBoard (Phase 2)
- Local SQLite database for user management and audit logs

## Quick Start

```bash
# Install system dependencies (Ubuntu/Debian):
sudo apt-get update
sudo apt-get install -y \
    build-essential python3-dev \
    patchelf ccache libfuse2

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your PLC IP and settings

# Run application
python scripts/db_initialize.py
python test/plc_simulator.py
python src/main.py

```

## Documentation

Complete technical documentation is available in the [Doc/](Doc/) folder:

- [Production Deploy Guide](deploy/README.md) - คู่มือ production สำหรับทีม Customer Service / Installer
- [Doc/SYSTEM_ARCHITECTURE.md](Doc/SYSTEM_ARCHITECTURE.md) - Complete system architecture
- [Doc/PLC_COMMUNICATION_SPEC.md](Doc/PLC_COMMUNICATION_SPEC.md) - Modbus TCP protocol
- [Doc/ALARM_SYSTEM_SPEC.md](Doc/ALARM_SYSTEM_SPEC.md) - 44 alarm blocks specification
- [Doc/THINGSBOARD_INTEGRATION.md](Doc/THINGSBOARD_INTEGRATION.md) - IoT platform integration
- [Doc/IMPLEMENTATION_ROADMAP.md](Doc/IMPLEMENTATION_ROADMAP.md) - 9-month development timeline
- [Doc/PROJECT_SUMMARY.md](Doc/PROJECT_SUMMARY.md) - Executive summary (Thai/English)
- [Doc/FONT_MANAGEMENT.md](Doc/FONT_MANAGEMENT.md) - Font bundling and management guide

## Development

See [CLAUDE.md](CLAUDE.md) for AI development guidelines and [StandardCoding_Python.md](StandardCoding_Python.md) for coding standards.

## License

Copyright © 2026 Adasoft. All rights reserved.
