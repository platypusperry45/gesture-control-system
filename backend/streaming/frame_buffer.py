"""
Thread-safe shared frame buffer.
"""

from __future__ import annotations

import threading


class FrameBuffer:

    def __init__(self):

        self._lock = threading.Lock()

        self._frame = None

    # -------------------------------------

    def write(self, frame):

        with self._lock:

            self._frame = frame

    # -------------------------------------

    def read(self):

        with self._lock:

            return None if self._frame is None else self._frame.copy()