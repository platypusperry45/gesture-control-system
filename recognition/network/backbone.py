"""
CNN backbone for gesture recognition.

Extracts image features from RGB gesture images.
"""

from __future__ import annotations

import tensorflow as tf

from .blocks import ConvBlock
from .blocks import ResidualBlock

layers = tf.keras.layers


class CNNBackbone(tf.keras.Model):
    """
    Lightweight residual CNN.
    """

    def __init__(self):

        super().__init__()

        # Initial feature extraction
        self.stem = ConvBlock(
            filters=32,
            kernel_size=3,
        )

        # Stage 1
        self.stage1 = [
            ResidualBlock(32),
            ResidualBlock(32),
        ]

        # Stage 2
        self.down2 = ConvBlock(
            filters=64,
            strides=2,
        )

        self.stage2 = [
            ResidualBlock(64),
            ResidualBlock(64),
        ]

        # Stage 3
        self.down3 = ConvBlock(
            filters=128,
            strides=2,
        )

        self.stage3 = [
            ResidualBlock(128),
            ResidualBlock(128),
        ]

        # Stage 4
        self.down4 = ConvBlock(
            filters=256,
            strides=2,
        )

        self.stage4 = [
            ResidualBlock(256),
            ResidualBlock(256),
        ]

        self.pool = layers.GlobalAveragePooling2D()

    def call(
        self,
        inputs,
        training=False,
    ):

        x = self.stem(
            inputs,
            training=training,
        )

        for block in self.stage1:

            x = block(
                x,
                training=training,
            )

        x = self.down2(
            x,
            training=training,
        )

        for block in self.stage2:

            x = block(
                x,
                training=training,
            )

        x = self.down3(
            x,
            training=training,
        )

        for block in self.stage3:

            x = block(
                x,
                training=training,
            )

        x = self.down4(
            x,
            training=training,
        )

        for block in self.stage4:

            x = block(
                x,
                training=training,
            )

        x = self.pool(x)

        return x