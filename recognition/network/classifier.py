"""
Gesture classifier.

Maps the fused feature representation to gesture probabilities.
"""

from __future__ import annotations

import tensorflow as tf

from .blocks import DenseBlock

layers = tf.keras.layers


class GestureClassifier(tf.keras.Model):
    """
    Final classification head.
    """

    def __init__(
        self,
        num_classes: int,
    ):

        super().__init__()

        self.block1 = DenseBlock(
            units=128,
            dropout=0.30,
        )

        self.block2 = DenseBlock(
            units=64,
            dropout=0.20,
        )

        self.output_layer = layers.Dense(
            units=num_classes,
            activation="softmax",
            kernel_initializer="glorot_uniform",
            name="gesture_output",
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

        x = self.output_layer(x)

        return x