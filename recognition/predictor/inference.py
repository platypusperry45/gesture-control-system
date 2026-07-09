"""
Real-Time Gesture Recognition Inference.
"""

from __future__ import annotations

import time
from pathlib import Path

from vision import VisionPipeline

from .model_loader import ModelLoader
from .predictor import Predictor
from .visualizer import Visualizer
ActionManager = None

class InferenceEngine:
    """
    Stateless inference engine.

    Input:
        frame (OpenCV BGR image)

    Output:
        {
            "gesture": ...,
            "confidence": ...,
            "action": ...,
            "frame": annotated_frame,
            "prediction": prediction
        }
    """

    def __init__(
        self,
        checkpoint_path: str | Path,
        class_names: list[str],
    ):

        self.model = ModelLoader(
            num_classes=len(class_names),
            checkpoint_path=checkpoint_path,
        ).load()

        self.pipeline = VisionPipeline()

        self.predictor = Predictor(
            model=self.model,
            class_names=class_names,
            pipeline=self.pipeline,
        )

        self.visualizer = Visualizer()


        try:
           from recognition.actions.action_manager import ActionManager

           self.action_manager = ActionManager()

        except Exception:

           self.action_manager = None

        # ---------------------------------------
        # Gesture confirmation
        # ---------------------------------------

        self.current_gesture = None
        self.gesture_start_time = None
        self.action_triggered = False

        self.confirmation_time = 0.4

        self.last_action = ""
        self.action_time = 0

        self._fps = 0.0

    # =====================================================
    # Predict One Frame
    # =====================================================

    def predict(self, frame):

        start = time.time()

        prediction = self.predictor.predict(frame)

        action = None

        # ---------------------------------------
        # No hand detected
        # ---------------------------------------

        if prediction is None:

            self.current_gesture = None
            self.gesture_start_time = None
            self.action_triggered = False

            fps = self._fps
            self._fps = 1.0 / max(time.time() - start, 1e-6)

            return {

                "gesture": None,

                "confidence": 0.0,

                "action": None,

                "fps": fps,

                "hand_detected": False,

                "frame": frame,

                "prediction": None,

            }

        gesture = prediction["gesture"]
        confidence = float(prediction["confidence"])

        print(f"[Prediction] {gesture} ({confidence:.3f})")

        # ---------------------------------------
        # Gesture confirmation
        # ---------------------------------------

        if confidence >= 0.90:

            print("[INFO] Confidence threshold passed.")

            if gesture != self.current_gesture:

                self.current_gesture = gesture
                self.gesture_start_time = time.time()
                self.action_triggered = False

                print(f"[INFO] New gesture: {gesture}")

            else:

                elapsed = time.time() - self.gesture_start_time

                print(f"[INFO] Holding {gesture} for {elapsed:.2f}s")

                if (
                    elapsed >= self.confirmation_time
                    and not self.action_triggered
                ):

                    print("[INFO] Executing action...")

                    if self.action_manager:

                       self.action_manager.execute(gesture)

                    self.last_action = gesture
                    self.action_time = time.time()

                    self.action_triggered = True

                    action = gesture

        else:

            print("[INFO] Confidence below threshold.")

            self.current_gesture = None
            self.gesture_start_time = None
            self.action_triggered = False

        # ---------------------------------------
        # Draw overlays
        # ---------------------------------------

        self.visualizer.draw(
            frame,
            prediction,
            prediction["hand"].landmarks,
        )

        fps = self._fps
        self._fps = 1.0 / max(time.time() - start, 1e-6)

        return {

            "gesture": gesture,

            "confidence": confidence,

            "action": self.last_action,

            "fps": fps,

            "hand_detected": True,

            "frame": frame,

            "prediction": prediction,

        }

    # =====================================================
    # Cleanup
    # =====================================================

    def close(self):

        self.predictor.close()