"""
MJPEG Camera Stream
"""

from __future__ import annotations

import cv2


class CameraStreamer:

    def __init__(self):

        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():

            raise RuntimeError("Unable to open camera.")

    def generate(self):

        while True:

            success, frame = self.camera.read()

            if not success:
                break

            _, buffer = cv2.imencode(
                ".jpg",
                frame,
            )

            frame_bytes = buffer.tobytes()

            yield (

                b"--frame\r\n"

                b"Content-Type: image/jpeg\r\n\r\n"

                + frame_bytes +

                b"\r\n"

            )

    def release(self):

        self.camera.release()