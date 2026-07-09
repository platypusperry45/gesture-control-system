"""
MJPEG Camera Stream
"""

from __future__ import annotations

import cv2
import time

class CameraStreamer:

    def __init__(
        self,
        engine,
        system_state,
    ):

        self.engine = engine

        self.system_state = system_state

        self.camera = cv2.VideoCapture(0)
        
        self.last_frame_time = time.perf_counter()

        self.fps = 0.0

        if not self.camera.isOpened():

            raise RuntimeError("Unable to open camera.")

    def generate(self):

        while True:

            success, frame = self.camera.read()

            if not success:
                break

            now = time.perf_counter()

            self.fps = 1.0 / max(
                now - self.last_frame_time,
                1e-6,
            )

            self.last_frame_time = now

            result = self.engine.predict(frame)

            annotated = result["frame"]

            # ------------------------------------
            # Update backend state
            # ------------------------------------

            self.system_state["camera"] = True

            self.system_state["model_loaded"] = True

            self.system_state["inference_running"] = True

            self.system_state["prediction"] = result["gesture"]

            self.system_state["confidence"] = float(
                result["confidence"]
            )

            self.system_state["action"] = result["action"]

            self.system_state["fps"] = round(
                self.fps,
                1,
            )

            self.system_state["hand_detected"] = result[
                "hand_detected"
            ]

            _, buffer = cv2.imencode(
                ".jpg",
                annotated,
            )

            yield (

                b"--frame\r\n"

                b"Content-Type: image/jpeg\r\n\r\n"

                + buffer.tobytes()

                + b"\r\n"

            )

    def release(self):

        self.camera.release()