"""
Model Loader.

Loads trained GestureRecognitionModel weights.
"""

from __future__ import annotations

from pathlib import Path

import tensorflow as tf

from recognition.network import GestureRecognitionModel


class ModelLoader:
    """
    Loads a trained gesture recognition model.
    """

    def __init__(
        self,
        num_classes: int,
        checkpoint_path: str | Path,
    ):

        self.num_classes = num_classes

        self.checkpoint_path = Path(checkpoint_path)

        self.model = None

        self.loaded = False

    def load(self) -> GestureRecognitionModel:

        if self.loaded:
            return self.model

        if not self.checkpoint_path.exists():
            raise FileNotFoundError(
                f"Checkpoint not found: {self.checkpoint_path}"
            )

        print("=" * 60)
        print("Loading Gesture Recognition Model")
        print("=" * 60)

        model = GestureRecognitionModel.build_model(
            num_classes=self.num_classes,
        )

        model.load_weights(
            self.checkpoint_path,
        )

        dummy = {
            "image": tf.zeros(
                (
                    1,
                    160,
                    160,
                    3,
                ),
                dtype=tf.float32,
            ),
            "landmarks": tf.zeros(
                (
                    1,
                    63,
                ),
                dtype=tf.float32,
            ),
        }

        model(dummy, training=False)

        self.model = model

        self.loaded = True

        print("Model loaded successfully.")

        return self.model