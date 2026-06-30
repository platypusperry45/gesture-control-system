"""
Gesture Predictor.

Runs end-to-end inference on a single image.
"""

from __future__ import annotations

import numpy as np
import tensorflow as tf

from recognition.network import GestureRecognitionModel
from vision import VisionPipeline
from .preprocessor import Preprocessor


class Predictor:
    """
    High-level inference pipeline.
    """

    def __init__(
        self,
        model: GestureRecognitionModel,
        class_names: list[str],
        pipeline: VisionPipeline,
    ):
        self.model = model
        self.class_names = class_names
        self.pipeline = pipeline

        self.preprocessor = Preprocessor()

        # compiled inference graph
        self._infer = tf.function(self._infer_step)

    # =====================================================
    # Predict
    # =====================================================

    def predict(self, image: np.ndarray) -> dict | None:

        # Vision pipeline (detection + landmarks)
        result = self.pipeline.process(image)

        if not result.hands:
            return None

        hand = result.hands[0]

        # Preprocess model inputs
        inputs = self.preprocessor.preprocess(
            image,
            landmarks=hand.landmarks,
        )

        # Optimized inference
        probabilities = self._infer(inputs).numpy()[0]

        predicted_index = int(np.argmax(probabilities))
        confidence = float(probabilities[predicted_index])

        return {
            "gesture": self.class_names[predicted_index],
            "label": predicted_index,
            "confidence": confidence,
            "probabilities": probabilities,
            "handedness": hand.handedness,
            "bounding_box": hand.bounding_box,
            "hand": hand,
        }

    # =====================================================
    # TF Graph Step
    # =====================================================

    def _infer_step(self, inputs):
        logits = self.model(inputs, training=False)
        return tf.nn.softmax(logits, axis=-1)

    # =====================================================
    # Cleanup
    # =====================================================

    def close(self):
        self.pipeline.close()