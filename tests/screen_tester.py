#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Screen Tester / Screenshot Tool for A9 screens.

Usage:
    python tests/screen_tester.py --list
    python tests/screen_tester.py --screen home
    python tests/screen_tester.py --screen home --capture
    python tests/screen_tester.py --capture-all
    python tests/screen_tester.py --screen home --offscreen
"""

from __future__ import annotations

import argparse
import importlib
import inspect
import os
import sys
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Project root setup
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ScreenInfo:
    stem: str           # e.g. "home", "login"
    module_name: str    # e.g. "src.ui.screens.home_ui"
    class_name: str     # e.g. "Ui_Screen01Home"
    label: str          # human-readable label


# ---------------------------------------------------------------------------
# Argument parsing  (must happen before Qt is imported)
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="A9 HMI Screen Tester / Screenshot Tool"
    )
    parser.add_argument(
        "--screen", "-s",
        type=str,
        help="Open a specific screen by stem name (e.g. home, login, user_lists)",
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all discovered screens and exit",
    )
    parser.add_argument(
        "--capture",
        action="store_true",
        help="Capture the selected --screen to PNG and exit",
    )
    parser.add_argument(
        "--capture-all",
        action="store_true",
        help="Capture all discovered screens to PNG and exit",
    )
    parser.add_argument(
        "--output-dir",
        default=str(PROJECT_ROOT / "tests" / "screenshots"),
        help="Directory for PNG output (default: tests/screenshots)",
    )
    parser.add_argument(
        "--delay-ms",
        type=int,
        default=300,
        help="Wait time after show() before capture in ms (default: 300)",
    )
    parser.add_argument(
        "--offscreen",
        action="store_true",
        help="Force QT_QPA_PLATFORM=offscreen (no display required)",
    )
    return parser.parse_args()


ARGS = parse_args()

if (ARGS.offscreen or ARGS.capture or ARGS.capture_all) and "QT_QPA_PLATFORM" not in os.environ:
    os.environ["QT_QPA_PLATFORM"] = "offscreen"


# ---------------------------------------------------------------------------
# Qt imports  (after env vars are set)
# ---------------------------------------------------------------------------

from PySide6.QtCore import QEventLoop, Qt, QTimer, Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


# ---------------------------------------------------------------------------
# Screen discovery
# ---------------------------------------------------------------------------

SCREEN_UI_DIR = PROJECT_ROOT / "src" / "ui" / "screens"


def discover_screens() -> dict[str, ScreenInfo]:
    """
    Discover all *_ui.py files in src/ui/screens and find their QMainWindow class.
    Returns a dict keyed by stem (e.g. "home", "login").
    """
    registry: dict[str, ScreenInfo] = {}

    for path in sorted(SCREEN_UI_DIR.glob("*_ui.py")):
        stem = path.stem.replace("_ui", "")          # "home_ui" -> "home"
        module_name = f"src.ui.screens.{path.stem}"  # "src.ui.screens.home_ui"

        try:
            module = importlib.import_module(module_name)
        except Exception as exc:
            print(f"[WARN] Could not import {module_name}: {exc}")
            continue

        class_name = _find_ui_class_name(module)
        if class_name is None:
            continue

        registry[stem] = ScreenInfo(
            stem=stem,
            module_name=module_name,
            class_name=class_name,
            label=stem.replace("_", " ").title(),
        )

    return dict(sorted(registry.items()))


def _find_ui_class_name(module: Any) -> Optional[str]:
    """
    Find the Ui_* class that has a setupUi() method inside the given module.
    Falls back to looking for any class with 'Ui_' prefix.
    """
    candidates: list[str] = []

    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ != module.__name__:
            continue
        # pyside6-uic generates classes named Ui_<ClassName>
        if name.startswith("Ui_") and hasattr(obj, "setupUi"):
            candidates.append(name)

    if not candidates:
        return None

    candidates.sort()
    return candidates[0]


# ---------------------------------------------------------------------------
# Screen instantiation
# ---------------------------------------------------------------------------

def instantiate_screen(screen_info: ScreenInfo) -> QMainWindow:
    """
    Create a bare QMainWindow and apply the generated Ui class to it.
    Works with the standard pyside6-uic output pattern:
        ui = Ui_ScreenXxx()
        ui.setupUi(window)
    """
    module = importlib.import_module(screen_info.module_name)
    ui_class = getattr(module, screen_info.class_name)

    window = QMainWindow()
    ui = ui_class()
    ui.setupUi(window)
    # Keep a reference so the ui object isn't GC'd while the window is open
    window._ui = ui
    return window


# ---------------------------------------------------------------------------
# Capture helpers
# ---------------------------------------------------------------------------

def wait_ms(delay_ms: int) -> None:
    loop = QEventLoop()
    QTimer.singleShot(delay_ms, loop.quit)
    loop.exec()


def capture_screen(
    app: QApplication,
    screen_info: ScreenInfo,
    output_dir: Path,
    delay_ms: int,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    window = instantiate_screen(screen_info)

    try:
        window.show()
        window.activateWindow()
        app.processEvents()
        wait_ms(delay_ms)
        app.processEvents()

        output_path = output_dir / f"{screen_info.stem}.png"
        pixmap = window.grab()
        if pixmap.isNull():
            raise RuntimeError("grab() returned an empty pixmap")
        if not pixmap.save(str(output_path), "PNG"):
            raise RuntimeError(f"Failed to save PNG to {output_path}")
        return output_path
    finally:
        window.close()
        window.deleteLater()
        app.processEvents()


# ---------------------------------------------------------------------------
# Main GUI - ScreenTester window
# ---------------------------------------------------------------------------

class ScreenTester(QMainWindow):
    """Simple GUI launcher to open any discovered screen."""

    def __init__(self, registry: dict[str, ScreenInfo]):
        super().__init__()
        self.registry = registry
        self.current_window: Optional[QMainWindow] = None

        self.setWindowTitle("A9 HMI Screen Tester")
        self.setMinimumSize(700, 480)
        self.setStyleSheet("background-color: #f5f5f5;")
        self._setup_ui()

    # ------------------------------------------------------------------
    def _setup_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(16)
        main_layout.setContentsMargins(30, 24, 30, 24)

        # Title
        title = QLabel("A9 HMI Screen Tester")
        title.setFont(QFont("Poppins", 22, QFont.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #003057;")
        main_layout.addWidget(title)

        subtitle = QLabel("เลือกหน้าจอเพื่อเปิดดู หรือใช้ --capture-all เพื่อบันทึก PNG ทั้งหมด")
        subtitle.setFont(QFont("Poppins", 12))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: #666;")
        main_layout.addWidget(subtitle)

        # Grid of screen buttons
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setStyleSheet("background: transparent;")

        scroll_widget = QWidget()
        grid = QGridLayout(scroll_widget)
        grid.setSpacing(12)

        row, col = 0, 0
        for stem, screen_info in self.registry.items():
            btn = self._make_screen_button(stem, screen_info)
            grid.addWidget(btn, row, col)
            col += 1
            if col >= 3:
                row += 1
                col = 0

        scroll.setWidget(scroll_widget)
        main_layout.addWidget(scroll)

        # Dropdown selector
        selector_group = QGroupBox("หรือเลือกจากรายการ")
        selector_group.setFont(QFont("Poppins", 11))
        selector_layout = QHBoxLayout(selector_group)

        self.screen_combo = QComboBox()
        self.screen_combo.setFont(QFont("Poppins", 12))
        self.screen_combo.setMinimumHeight(40)
        for stem, screen_info in self.registry.items():
            self.screen_combo.addItem(
                f"{screen_info.label}  [{screen_info.class_name}]",
                stem,
            )
        selector_layout.addWidget(self.screen_combo, stretch=1)

        open_btn = QPushButton("เปิดหน้าจอ")
        open_btn.setFont(QFont("Poppins", 12, QFont.Bold))
        open_btn.setMinimumHeight(40)
        open_btn.setMinimumWidth(130)
        open_btn.setStyleSheet("""
            QPushButton {
                background-color: #003057;
                color: white;
                border-radius: 8px;
                padding: 8px 20px;
            }
            QPushButton:hover  { background-color: #004B93; }
            QPushButton:pressed { background-color: #002040; }
        """)
        open_btn.clicked.connect(self._on_open_selected)
        selector_layout.addWidget(open_btn)

        main_layout.addWidget(selector_group)

        # Footer info
        info = QLabel(f"ตรวจพบ {len(self.registry)} screen จาก src/ui/screens")
        info.setFont(QFont("Poppins", 10))
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info.setStyleSheet("color: #999;")
        main_layout.addWidget(info)

    # ------------------------------------------------------------------
    def _make_screen_button(self, stem: str, info: ScreenInfo) -> QPushButton:
        btn = QPushButton()
        btn.setMinimumSize(190, 90)
        btn.setFont(QFont("Poppins", 10))
        btn.setText(f"{info.label}\n{info.class_name}")
        btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 3px solid #003057;
                border-radius: 12px;
                padding: 10px;
                color: #003057;
            }
            QPushButton:hover  { background-color: #e8f4f8; border-color: #004B93; }
            QPushButton:pressed { background-color: #d0e8f0; }
        """)
        btn.clicked.connect(lambda _checked=False, s=stem: self._open_screen(s))
        return btn

    # ------------------------------------------------------------------
    @Slot()
    def _on_open_selected(self) -> None:
        stem = self.screen_combo.currentData()
        if stem:
            self._open_screen(str(stem))

    def _open_screen(self, stem: str) -> None:
        if stem not in self.registry:
            QMessageBox.warning(self, "ไม่พบหน้าจอ", f"ไม่พบ screen: {stem}")
            return

        try:
            if self.current_window is not None:
                self.current_window.close()
                self.current_window.deleteLater()

            self.current_window = instantiate_screen(self.registry[stem])
            self.current_window.show()

        except Exception as exc:
            QMessageBox.critical(
                self,
                "Error",
                f"เปิด screen '{stem}' ไม่สำเร็จ\n\n{exc}",
            )
            traceback.print_exc()


# ---------------------------------------------------------------------------
# CLI modes
# ---------------------------------------------------------------------------

def list_screens(registry: dict[str, ScreenInfo]) -> int:
    print("\n" + "=" * 70)
    print("A9 HMI - Discovered screens")
    print("=" * 70)
    for stem, info in registry.items():
        print(f"  {info.label:<25}  class: {info.class_name}")
        print(f"    module: {info.module_name}")
    print("=" * 70)
    print(f"Total: {len(registry)} screens")
    print("=" * 70 + "\n")
    return 0


def run_single_screen(
    app: QApplication,
    registry: dict[str, ScreenInfo],
) -> int:
    stem = ARGS.screen
    if stem not in registry:
        print(f"[ERR] Screen '{stem}' not found. Use --list to see available screens.")
        return 1

    window = instantiate_screen(registry[stem])
    window.show()
    return app.exec()


def run_single_capture(
    app: QApplication,
    registry: dict[str, ScreenInfo],
    output_dir: Path,
) -> int:
    stem = ARGS.screen
    if stem not in registry:
        print(f"[ERR] Screen '{stem}' not found. Use --list to see available screens.")
        return 1

    output_path = capture_screen(
        app=app,
        screen_info=registry[stem],
        output_dir=output_dir,
        delay_ms=ARGS.delay_ms,
    )
    print(f"[OK] Saved: {output_path}")
    return 0


def run_batch_capture(
    app: QApplication,
    registry: dict[str, ScreenInfo],
    output_dir: Path,
) -> int:
    failures: list[tuple[str, str]] = []

    for stem, screen_info in registry.items():
        try:
            output_path = capture_screen(
                app=app,
                screen_info=screen_info,
                output_dir=output_dir,
                delay_ms=ARGS.delay_ms,
            )
            print(f"[OK]   {stem:<25} -> {output_path.name}")
        except Exception as exc:
            failures.append((stem, str(exc)))
            print(f"[FAIL] {stem:<25} -> {exc}")
            traceback.print_exc()

    if failures:
        print("\nCapture completed with failures:")
        for stem, msg in failures:
            print(f"  - {stem}: {msg}")
        return 1

    print(f"\n[OK] Captured {len(registry)} screens to: {output_dir}")
    return 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    registry = discover_screens()

    if not registry:
        print("[ERR] No screens discovered in src/ui/screens")
        print("      Run: python scripts/compile_ui.py  first.")
        return 1

    if ARGS.list:
        return list_screens(registry)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    output_dir = Path(ARGS.output_dir)

    if ARGS.capture_all:
        return run_batch_capture(app, registry, output_dir)

    if ARGS.capture:
        if ARGS.screen is None:
            print("[ERR] --capture requires --screen <stem>")
            return 1
        return run_single_capture(app, registry, output_dir)

    if ARGS.screen is not None:
        return run_single_screen(app, registry)

    # Default: open the GUI launcher
    window = ScreenTester(registry)
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
