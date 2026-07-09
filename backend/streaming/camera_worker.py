"""
Background camera capture thread.
"""

from __future__ import annotations

import threading
import time

import cv2

from .frame_buffer import FrameBuffer


class CameraWorker:

    def __init__(
        self,
        frame_buffer: FrameBuffer,
        source: int = 0,
    ):

        self.frame_buffer = frame_buffer

        self.camera = cv2.VideoCapture(source)

        if not self.camera.isOpened():
            raise RuntimeError("Unable to open camera.")

        self.running = False

        self.thread = None

    # ------------------------------------------------

    def _capture_loop(self):

        while self.running:

            success, frame = self.camera.read()

            if not success:
                continue

            self.frame_buffer.write(frame)

            # tiny sleep prevents CPU spinning
            time.sleep(0.001)

    # ------------------------------------------------

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._capture_loop,
            daemon=True,
        )

        self.thread.start()

    # ------------------------------------------------

    def stop(self):

        self.running = False

        if self.thread is not None:
            self.thread.join(timeout=1)

        self.camera.release()