#!/bin/bash
# ==============================================================================
# NAM-WH HMI - Startup Script
# สคริปต์เริ่มต้นแอปพลิเคชัน NAM-WH HMI
# ==============================================================================
# ใช้งาน:
#   ./start.sh              - รันปกติ (production)
#   ./start.sh --dev        - รันในโหมด development
#   ./start.sh --fullscreen - รันแบบเต็มหน้าจอ
# ==============================================================================

set -e

# --- กำหนด Path ---
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/env"
MAIN_PY="$PROJECT_DIR/src/main.py"
LOG_DIR="$PROJECT_DIR/data/logs"
LOG_FILE="$LOG_DIR/startup.log"

# --- Parse Arguments ---
DEV_MODE=false
FULLSCREEN_OVERRIDE=false

for arg in "$@"; do
    case $arg in
        --dev)
            DEV_MODE=true
            ;;
        --fullscreen)
            FULLSCREEN_OVERRIDE=true
            ;;
    esac
done

# --- สร้าง log directory ถ้ายังไม่มี ---
mkdir -p "$LOG_DIR"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "======================================================"
log "เริ่มต้น NAM-WH HMI"
log "Project Dir: $PROJECT_DIR"
log "======================================================"

# --- ตรวจสอบ virtual environment ---
if [ ! -f "$VENV_DIR/bin/activate" ]; then
    log "[ERROR] ไม่พบ virtual environment ที่: $VENV_DIR"
    log "กรุณารัน: python3 -m venv $VENV_DIR && pip install -r requirements.txt"
    exit 1
fi

log "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# --- ตรวจสอบ main.py ---
if [ ! -f "$MAIN_PY" ]; then
    log "[ERROR] ไม่พบไฟล์: $MAIN_PY"
    exit 1
fi

# --- ตั้งค่า Environment Variables ---
export PYTHONPATH="$PROJECT_DIR/src:$PROJECT_DIR"
export PYTHONUNBUFFERED=1

# ตั้งค่า DISPLAY สำหรับ Raspberry Pi (Wayland/X11)
if [ -z "$DISPLAY" ] && [ -z "$WAYLAND_DISPLAY" ]; then
    export DISPLAY=:0
    log "ตั้งค่า DISPLAY=:0"
fi

# โหมด Development
if [ "$DEV_MODE" = true ]; then
    log "โหมด: Development"
    export DEBUG_MODE=true
    export LOG_LEVEL=DEBUG
    export MOCK_PLC=true
    export FULLSCREEN=false
else
    log "โหมด: Production"
fi

# บังคับ Fullscreen (ถ้าระบุ argument)
if [ "$FULLSCREEN_OVERRIDE" = true ]; then
    export FULLSCREEN=true
    log "เปิดใช้งาน Fullscreen mode"
fi

# --- รัน Application ---
log "กำลังเริ่มต้นแอปพลิเคชัน..."
cd "$PROJECT_DIR"

exec python "$MAIN_PY" 2>&1 | tee -a "$LOG_FILE"
