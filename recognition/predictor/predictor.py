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

        # TensorFlow compiled inference graph
        self._infer = tf.function(self._infer_step)

        # ---------- Temporal smoothing ----------
        self.current_prediction = None
        self.current_count = 0

        self.display_prediction = None

        # Tunable parameters
        self.confidence_threshold = 0.70
        self.required_consecutive = 2

    # =====================================================
    # Predict
    # =====================================================

    def predict(self, image: np.ndarray) -> dict | None:

        result = self.pipeline.process(image)

        if not result.hands:
            self.current_prediction = None
            self.current_count = 0
            self.display_prediction = None
            return None

        hand = result.hands[0]

        inputs = self.preprocessor.preprocess(
            hand.cropped_image,
            landmarks=hand.landmarks,
        )

        probabilities = self._infer(inputs).numpy()[0]

        predicted_index = int(np.argmax(probabilities))
        confidence = float(probabilities[predicted_index])

        # =====================================================
        # High confidence -> update immediately
        # =====================================================

        if confidence >= self.confidence_threshold:

            self.display_prediction = predicted_index
            self.current_prediction = predicted_index
            self.current_count = self.required_consecutive

        # =====================================================
        # Lower confidence -> require consistency
        # =====================================================

        else:

            if predicted_index == self.current_prediction:
                self.current_count += 1
            else:
                self.current_prediction = predicted_index
                self.current_count = 1

            if self.current_count >= self.required_consecutive:
                self.display_prediction = predicted_index

        # First prediction fallback
        if self.display_prediction is None:
            self.display_prediction = predicted_index

        final_index = self.display_prediction
        final_confidence = float(probabilities[final_index])

        return {
            "gesture": self.class_names[final_index],
            "label": final_index,
            "confidence": final_confidence,
            "probabilities": probabilities,
            "handedness": hand.handedness,
            "bounding_box": hand.bounding_box,
            "hand": hand,
        }

    # =====================================================
    # TF Graph
    # =====================================================

    def _infer_step(self, inputs):
        logits = self.model(inputs, training=False)
        return tf.nn.softmax(logits, axis=-1)

    # =====================================================
    # Cleanup
    # =====================================================

    def close(self):
        self.pipeline.close()