"""
FPS Counter Module.

Provides a rolling-average FPS counter for smooth
performance monitoring in real-time computer vision pipelines.

Author: Akshat Yadav
Project: Gesture-Based Desktop Control System
"""

from __future__ import annotations

import time
from collections import deque


class FPSCounter:
    """
    Computes a smoothed Frames Per Second (FPS).

    Uses a rolling average to reduce fluctuations.
    """

    def __init__(self, buffer_size: int = 30):
        self.buffer = deque(maxlen=buffer_size)
        self.previous_time = time.perf_counter()

    def update(self) -> float:
        """
        Update FPS measurement.

        Returns
        -------
        float
            Smoothed FPS.
        """

        current_time = time.perf_counter()

        elapsed = current_time - self.previous_time

        self.previous_time = current_time

        if elapsed <= 0:
            return 0.0

        fps = 1.0 / elapsed

        self.buffer.append(fps)

        return sum(self.buffer) / len(self.buffer)

    def reset(self):
        """Reset FPS history."""

        self.buffer.clear()
        self.previous_time = time.perf_counter()