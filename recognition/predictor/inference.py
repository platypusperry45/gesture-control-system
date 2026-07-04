"""
Real-Time Gesture Recognition Inference.
"""

from __future__ import annotations

import time
import cv2
from pathlib import Path

from vision import VisionPipeline

from recognition.actions.action_manager import ActionManager
from .camera import Camera
from .model_loader import ModelLoader
from .predictor import Predictor
from .visualizer import Visualizer


class InferenceEngine:
    """
    Runs real-time gesture recognition.
    """

    def __init__(
        self,
        checkpoint_path: str | Path,
        class_names: list[str],
        camera_source: int | str = 0,
    ):

        

        self.model = ModelLoader(
            num_classes=len(class_names),
        ).load(
            checkpoint_path,
        )

        

        self.pipeline = VisionPipeline()
        

        self.predictor = Predictor(
            model=self.model,
            class_names=class_names,
            pipeline=self.pipeline,
        )
        

        self.action_manager = ActionManager()
        

        self.visualizer = Visualizer()
        

        self.camera = Camera(
            source=camera_source,
        )
        

        self.running = True

        # -----------------------------------------
        # Gesture confirmation
        # -----------------------------------------
        self.current_gesture = None
        self.gesture_start_time = None
        self.action_triggered = False

        # Hold gesture for this many seconds
        self.confirmation_time = 0.4
        

        self.last_action = ""
        self.action_time = 0
    # =====================================================
    # Main Loop
    # =====================================================

    def run(self):

        print("Starting inference loop...")

        while self.running:

            frame = self.camera.read()

            if frame is None:
                break

            prediction = self.predictor.predict(frame)

            # -----------------------------------------
            # No hand detected
            # -----------------------------------------
            if prediction is None:

                self.current_gesture = None
                self.gesture_start_time = None
                self.action_triggered = False

            else:

                gesture = prediction["gesture"]

                # Optional confidence threshold
                if prediction["confidence"] >= 0.90:

                    # New gesture
                    if gesture != self.current_gesture:

                        self.current_gesture = gesture
                        self.gesture_start_time = time.time()
                        self.action_triggered = False

                    else:

                        elapsed = (
                            time.time()
                            - self.gesture_start_time
                        )

                        if (
                            elapsed >= self.confirmation_time
                            and not self.action_triggered
                        ):

                            self.action_manager.execute(
                                gesture
                            )
                            self.last_action = gesture
                            self.action_time = time.time()
                            self.action_triggered = True

                else:
                    # Confidence dropped
                    self.current_gesture = None
                    self.gesture_start_time = None
                    self.action_triggered = False

                # Draw visualization
                self.visualizer.draw(
                    frame,
                    prediction,
                    prediction["hand"].landmarks,
                )

            self.camera.show(
                "Gesture Recognition",
                frame,
            )
            if time.time() - self.action_time < 1.0:

               cv2.putText(
                   frame,
                   f"Action : {self.last_action}",
                   (20, 80),
                   cv2.FONT_HERSHEY_SIMPLEX,
                   0.9,
                   (0,255,0),
                   2,
                )
            if self.camera.should_close():
                break

        self.close()

    # =====================================================
    # Cleanup
    # =====================================================

    def close(self):

        self.predictor.close()
        self.camera.close()


# ==========================================================
# Main
# ==========================================================

def main():

    checkpoint = (
        "recognition/artifacts/checkpoints/best.weights.h5"
    )

    class_names = [
        "open_palm",
        "fist",
        "peace",
        "thumbs_up",
        "point",
        "okay",
    ]

    engine = InferenceEngine(
        checkpoint_path=checkpoint,
        class_names=class_names,
    )

    engine.run()


if __name__ == "__main__":
    main()