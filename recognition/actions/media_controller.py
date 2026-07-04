import pyautogui


class MediaController:
    """
    Controls media playback.
    """

    @staticmethod
    def play_pause():
        pyautogui.press("playpause")

    @staticmethod
    def next_track():
        pyautogui.press("nexttrack")

    @staticmethod
    def previous_track():
        pyautogui.press("prevtrack")