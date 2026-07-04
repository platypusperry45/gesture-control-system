from datetime import datetime
from pathlib import Path

import pyautogui


class KeyboardController:

    @staticmethod
    def screenshot():

        # Create screenshots folder
        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True)

        # Timestamped filename
        filename = screenshot_dir / datetime.now().strftime(
            "Screenshot_%Y-%m-%d_%H-%M-%S.png"
        )

        # Capture screen
        pyautogui.screenshot(str(filename))

        print(f"Screenshot saved: {filename}")