"""
Cooldown manager.

Prevents the same action from being triggered repeatedly
within a short period of time.
"""

from __future__ import annotations

import time


class Cooldown:
    """
    Generic cooldown timer.
    """

    def __init__(self, seconds: float = 1.0):
        self.seconds = seconds
        self.last_trigger = {}

    def ready(self, key: str) -> bool:

        now = time.time()

        if key not in self.last_trigger:
            self.last_trigger[key] = now
            return True

        if now - self.last_trigger[key] >= self.seconds:
            self.last_trigger[key] = now
            return True

        return False