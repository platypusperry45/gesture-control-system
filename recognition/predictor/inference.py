"""
Real-Time Gesture Recognition Inference.
"""

from __future__ import annotations

from pathlib import Path

from recognition.network import GestureRecognitionModel

from .camera import Camera
from .model_loader import ModelLoader
from .predictor import Predictor
from .visualizer import Visualizer
from queue import Queue
import threading

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

        self.predictor = Predictor(

            model=self.model,

            class_names=class_names,

        )

        self.visualizer = Visualizer()
        self.frame_queue = Queue(maxsize=2)
        self.running = True
        self.camera = Camera(

            source=camera_source,
        
        )

    # =====================================================
    # Main Loop
    # =====================================================

    def run(self):

        while True:

            frame = self.camera.read()

            if frame is None:

                break

            prediction = self.predictor.predict(frame)

            if prediction is not None:

               self.visualizer.draw(

                   frame,
 
                   prediction,

                   prediction["hand"].landmarks,

                )

            self.camera.show(

                "Gesture Recognition",

                frame,

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