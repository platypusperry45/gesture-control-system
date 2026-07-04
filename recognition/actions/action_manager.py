"""
Maps gestures to operating system actions.
"""

from __future__ import annotations

from .cooldown import Cooldown
from .media_controller import MediaController
from .volume_controller import VolumeController
from .keyboard_controller import KeyboardController


class ActionManager:

    def __init__(self):

        self.volume = VolumeController()

        self.cooldown = Cooldown(seconds=1.0)

    def execute(self, gesture: str):

        if not self.cooldown.ready(gesture):
            return

        if gesture == "thumbs_up":

            print("ACTION: Volume Up")

            self.volume.increase()

        elif gesture == "open_palm":

            print("ACTION: Mute")

            self.volume.mute()

        elif gesture == "fist":

            print("ACTION: Play/Pause")

            MediaController.play_pause()

        elif gesture == "peace":

            print("ACTION: Next Track")

            MediaController.next_track()

        elif gesture == "point":

            print("ACTION: Previous Track")

            MediaController.previous_track()

        elif gesture == "okay":

            print("ACTION: Screenshot")

            KeyboardController.screenshot()