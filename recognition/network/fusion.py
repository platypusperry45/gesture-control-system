"""
Feature fusion module.

Combines image features and landmark features into
a single embedding for classification.
"""

from __future__ import annotations

import tensorflow as tf

from .blocks import DenseBlock

layers = tf.keras.layers


class FeatureFusion(tf.keras.Model):
    """
    Fuses image and landmark embeddings.
    """

    def __init__(self):

        super().__init__()

        self.concat = layers.Concatenate()

        self.block1 = DenseBlock(
            units=256,
            dropout=0.40,
        )

        self.block2 = DenseBlock(
            units=128,
            dropout=0.30,
        )

    def call(
        self,
        image_features,
        landmark_features,
        training=False,
    ):

        x = self.concat(
            [
                image_features,
                landmark_features,
            ]
        )

        x = self.block1(
            x,
            training=training,
        )

        x = self.block2(
            x,
            training=training,
        )

        return x