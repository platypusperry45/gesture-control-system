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
        prediction_counts,
        fps_history,
        confidence_history,
    ):

        self.engine = engine

        self.system_state = system_state

        self.prediction_counts = prediction_counts

        self.fps_history = fps_history

        self.confidence_history = confidence_history


        self.camera = cv2.VideoCapture(0)


        self.last_frame_time = time.perf_counter()

        self.fps = 0.0



        if not self.camera.isOpened():

            raise RuntimeError(
                "Unable to open camera."
            )



    def generate(self):


        while True:


            success, frame = self.camera.read()


            if not success:

                break



            now = time.perf_counter()


            self.fps = (
                1.0 /
                max(
                    now-self.last_frame_time,
                    1e-6
                )
            )


            self.last_frame_time = now



            result = self.engine.predict(frame)



            gesture = result.get(
                "gesture"
            )


            confidence = float(
                result.get(
                    "confidence",
                    0
                )
            )



            action = result.get(
                "action"
            )



            annotated = result["frame"]



            # -----------------------------
            # Backend Analytics Update
            # -----------------------------


            self.system_state["camera"] = True

            self.system_state["inference_running"] = True

            self.system_state["prediction"] = gesture

            self.system_state["confidence"] = confidence

            self.system_state["action"] = action

            self.system_state["fps"] = round(
                self.fps,
                1
            )

            self.system_state["hand_detected"] = result.get(
                "hand_detected",
                False
            )



            if gesture:


                self.prediction_counts[gesture] = (
                    self.prediction_counts.get(
                        gesture,
                        0
                    )
                    + 1
                )



            self.fps_history.append(
                round(
                    self.fps,
                    1
                )
            )


            self.confidence_history.append(
                round(
                    confidence,
                    3
                )
            )



            _, buffer = cv2.imencode(
                ".jpg",
                annotated
            )



            yield (

                b"--frame\r\n"

                b"Content-Type: image/jpeg\r\n\r\n"

                +

                buffer.tobytes()

                +

                b"\r\n"

            )



    def release(self):

        self.camera.release()