"""
Background inference service.

Runs gesture recognition continuously in a separate thread.
"""

from __future__ import annotations

import threading
import time

from vision import VisionPipeline

from recognition.predictor.camera import Camera
from recognition.predictor.model_loader import ModelLoader
from recognition.predictor.predictor import Predictor


class InferenceService:

    def __init__(self):

        self.running = False
        self.thread = None

        self.camera = None
        self.pipeline = None
        self.predictor = None

        self.latest_prediction = None
        self.latest_fps = 0.0

    # -------------------------------------------------

    def start(
        self,
        checkpoint_path: str,
        class_names: list[str],
        camera_source: int = 0,
    ):

        if self.running:
            return

        print("Loading model...")

        model = ModelLoader(
            num_classes=len(class_names),
        ).load(
            checkpoint_path,
        )

        print("Model loaded")

        self.pipeline = VisionPipeline()

        self.predictor = Predictor(
            model=model,
            class_names=class_names,
            pipeline=self.pipeline,
        )

        self.camera = Camera(
            source=camera_source,
        )

        self.running = True

        self.thread = threading.Thread(
            target=self._loop,
            daemon=True,
        )

        self.thread.start()

        print("Inference service started.")

    # -------------------------------------------------

    def stop(self):

        self.running = False

        if self.thread is not None:
            self.thread.join(timeout=2)

        if self.predictor is not None:
            self.predictor.close()

        if self.camera is not None:
            self.camera.close()

        print("Inference service stopped.")

    # -------------------------------------------------

    def _loop(self):

        previous = time.time()

        while self.running:

            frame = self.camera.read()

            if frame is None:
                continue

            prediction = self.predictor.predict(frame)

            self.latest_prediction = prediction

            now = time.time()

            dt = now - previous

            previous = now

            if dt > 0:
                self.latest_fps = 1.0 / dt

    # -------------------------------------------------

    def get_prediction(self):

        return self.latest_prediction

    # -------------------------------------------------

    def get_status(self):

        prediction = self.latest_prediction

        if prediction is None:

            return {

                "backend": "running",

                "camera": True,

                "model": True,

                "inference": self.running,

                "prediction": None,

                "confidence": 0.0,

                "fps": round(self.latest_fps, 1),

            }

        return {

            "backend": "running",

            "camera": True,

            "model": True,

            "inference": self.running,

            "prediction": prediction["gesture"],

            "confidence": round(
                prediction["confidence"],
                3,
            ),

            "fps": round(
                self.latest_fps,
                1,
            ),

        }