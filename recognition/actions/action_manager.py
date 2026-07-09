"""
Dynamic Action Manager

Loads gesture mappings from backend/data/action_mappings.json
"""

from __future__ import annotations

import json
from pathlib import Path

from .cooldown import Cooldown
from .keyboard_controller import KeyboardController
from .media_controller import MediaController
from .volume_controller import VolumeController
from .mouse_controller import MouseController


class ActionManager:

    def __init__(self):

        self.cooldown = Cooldown(seconds=1.0)

        self.volume = VolumeController()

        self.mapping_file = (
            Path(__file__).resolve().parents[2]
            / "backend"
            / "data"
            / "action_mappings.json"
        )

    # -------------------------------------------------
    # Load Mapping File
    # -------------------------------------------------

    def load_mapping(self):

        if not self.mapping_file.exists():
            return {}

        try:

            with open(
                self.mapping_file,
                "r",
                encoding="utf-8",
            ) as f:

                return json.load(f)

        except Exception:

            return {}

    # -------------------------------------------------
    # Execute Gesture
    # -------------------------------------------------

    def execute(self, gesture: str):

        if not self.cooldown.ready(gesture):
            return

        mappings = self.load_mapping()

        mapping = mappings.get(gesture)

        if mapping is None:
            return

        if not mapping.get("enabled", True):
            return

        action_type = mapping["type"]
        action = mapping["action"]

        print(f"{gesture} -> {action}")

        if action_type == "Keyboard":

            self.execute_keyboard(action)

        elif action_type == "Media":

            self.execute_media(action)

        elif action_type == "Mouse":

            self.execute_mouse(action)

        elif action_type == "Browser":

            self.execute_browser(action)

        elif action_type == "System":

            self.execute_system(action)

    # -------------------------------------------------
    # Keyboard
    # -------------------------------------------------

    def execute_keyboard(self, action):

        keyboard = {

            "Ctrl+C": ("ctrl", "c"),
            "Ctrl+V": ("ctrl", "v"),
            "Ctrl+X": ("ctrl", "x"),
            "Ctrl+Z": ("ctrl", "z"),
            "Ctrl+Y": ("ctrl", "y"),
            "Alt+Tab": ("alt", "tab"),
            "Win+D": ("win", "d"),

        }

        if action == "Screenshot":

            KeyboardController.screenshot()

            return

        if action in keyboard:

            KeyboardController.hotkey(*keyboard[action])

    # -------------------------------------------------
    # Media
    # -------------------------------------------------

    def execute_media(self, action):

        if action == "Play/Pause":

            MediaController.play_pause()

        elif action == "Next Track":

            MediaController.next_track()

        elif action == "Previous Track":

            MediaController.previous_track()

        elif action == "Volume Up":

            self.volume.increase()

        elif action == "Volume Down":

            self.volume.decrease()

        elif action == "Mute":

            self.volume.mute()

    # -------------------------------------------------
    # Mouse
    # -------------------------------------------------

    def execute_mouse(self, action):

        if action == "Left Click":

            MouseController.left_click()

        elif action == "Right Click":

            MouseController.right_click()

        elif action == "Double Click":

            MouseController.double_click()

    # -------------------------------------------------
    # Browser
    # -------------------------------------------------

    def execute_browser(self, action):

        if action == "New Tab":

            KeyboardController.hotkey("ctrl", "t")

        elif action == "Close Tab":

            KeyboardController.hotkey("ctrl", "w")

        elif action == "Refresh":

            KeyboardController.press("f5")

        elif action == "Back":

            KeyboardController.hotkey("alt", "left")

        elif action == "Forward":

            KeyboardController.hotkey("alt", "right")

    # -------------------------------------------------
    # System
    # -------------------------------------------------

    def execute_system(self, action):

        if action == "Screenshot":

            KeyboardController.screenshot()

        elif action == "Lock PC":

            KeyboardController.hotkey("win", "l")

        elif action == "Sleep":

            print("Sleep not implemented yet.")