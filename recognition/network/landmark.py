"""
Landmark feature encoder.

Converts 63 MediaPipe landmark values
into a compact feature vector.
"""

from __future__ import annotations

import tensorflow as tf

from .blocks import DenseBlock

layers = tf.keras.layers


class LandmarkEncoder(tf.keras.Model):
    """
    Landmark feature extractor.
    """

    def __init__(self):

        super().__init__()

        self.block1 = DenseBlock(
            128,
            dropout=0.30,
        )

        self.block2 = DenseBlock(
            128,
            dropout=0.30,
        )

        self.block3 = DenseBlock(
            64,
            dropout=0.20,
        )

    def call(
        self,
        inputs,
        training=False,
    ):

        x = self.block1(
            inputs,
            training=training,
        )

        x = self.block2(
            x,
            training=training,
        )

        x = self.block3(
            x,
            training=training,
        )

        return x