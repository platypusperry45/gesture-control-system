"""
Complete Hybrid Gesture Recognition Network.

Combines:

- CNN image backbone
- Landmark encoder
- Feature fusion
- Gesture classifier
"""

from __future__ import annotations

import tensorflow as tf

from .backbone import CNNBackbone
from .landmark import LandmarkEncoder
from .fusion import FeatureFusion
from .classifier import GestureClassifier


class GestureRecognitionModel(tf.keras.Model):
    """
    Hybrid Gesture Recognition Network.

    Inputs
    ------
    image:
        (B,224,224,3)

    landmarks:
        (B,63)

    Output
    ------
    (B,num_classes)
    """

    def __init__(
        self,
        num_classes: int,
    ):

        super().__init__()

        self.image_backbone = CNNBackbone()

        self.landmark_encoder = LandmarkEncoder()

        self.fusion = FeatureFusion()

        self.classifier = GestureClassifier(
            num_classes=num_classes,
        )

    # =====================================================
    # Forward Pass
    # =====================================================

    def call(
        self,
        inputs,
        training=False,
    ):

        image = inputs["image"]

        landmarks = inputs["landmarks"]

        image_features = self.image_backbone(
            image,
            training=training,
        )

        landmark_features = self.landmark_encoder(
            landmarks,
            training=training,
        )

        fused_features = self.fusion(
            image_features,
            landmark_features,
            training=training,
        )

        predictions = self.classifier(
            fused_features,
            training=training,
        )

        return predictions

    # =====================================================
    # Utility
    # =====================================================

    @staticmethod
    def build_model(
        num_classes: int,
    ):

        model = GestureRecognitionModel(
            num_classes=num_classes,
        )

        dummy = {
            "image": tf.zeros(
                (
                    1,
                    224,
                    224,
                    3,
                )
            ),
            "landmarks": tf.zeros(
                (
                    1,
                    63,
                )
            ),
        }

        model(dummy)

        return model