"""
Real-Time Gesture Recognition Inference.
"""

from __future__ import annotations

from pathlib import Path

from vision import VisionPipeline

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

        print("Loading model...")

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
        

        self.visualizer = Visualizer()
        

        self.camera = Camera(
            source=camera_source,
        )
        

        self.running = True

    # =====================================================
    # Main Loop
    # =====================================================

    def run(self):

        print("Starting inference loop...")

        frame_count = 0

        while self.running:

            frame = self.camera.read()

            frame_count += 1


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
                print("Q pressed. Closing.")
                break

        self.close()

    # =====================================================
    # Cleanup
    # =====================================================

    def close(self):

        print("Closing predictor...")
        self.predictor.close()

        print("Closing camera...")
        self.camera.close()

        print("Finished cleanup.")


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