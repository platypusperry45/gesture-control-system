from datetime import datetime
from pathlib import Path

import pyautogui


class KeyboardController:

    @staticmethod
    def hotkey(*keys):
        """
        Execute a keyboard shortcut.

        Example:
            KeyboardController.hotkey("ctrl", "c")
            KeyboardController.hotkey("alt", "tab")
            KeyboardController.hotkey("win", "d")
        """

        try:

            pyautogui.hotkey(*keys)

            print(f"Hotkey executed: {' + '.join(keys)}")

        except Exception as e:

            print(f"Hotkey failed: {e}")

    @staticmethod
    def press(key):
        """
        Press a single keyboard key.
        """

        try:

            pyautogui.press(key)

            print(f"Key pressed: {key}")

        except Exception as e:

            print(f"Key press failed: {e}")

    @staticmethod
    def write(text):
        """
        Type text.
        """

        try:

            pyautogui.write(text)

            print(f"Typed: {text}")

        except Exception as e:

            print(f"Typing failed: {e}")

    @staticmethod
    def screenshot():
        """
        Save a timestamped screenshot.
        """

        screenshot_dir = Path("screenshots")

        screenshot_dir.mkdir(exist_ok=True)

        filename = screenshot_dir / datetime.now().strftime(
            "Screenshot_%Y-%m-%d_%H-%M-%S.png"
        )

        pyautogui.screenshot(str(filename))

        print(f"Screenshot saved: {filename}")