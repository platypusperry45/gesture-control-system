"""
Reusable neural network building blocks.

Every CNN component in the project is built using these blocks.
"""

from __future__ import annotations

import tensorflow as tf

layers = tf.keras.layers


# ==========================================================
# Conv → BatchNorm → ReLU
# ==========================================================

class ConvBlock(layers.Layer):

    def __init__(
        self,
        filters: int,
        kernel_size: int = 3,
        strides: int = 1,
        padding: str = "same",
    ):

        super().__init__()

        self.conv = layers.Conv2D(
            filters=filters,
            kernel_size=kernel_size,
            strides=strides,
            padding=padding,
            use_bias=False,
            kernel_initializer="he_normal",
        )

        self.bn = layers.BatchNormalization()

        self.relu = layers.ReLU()

    def call(
        self,
        inputs,
        training=False,
    ):

        x = self.conv(inputs)

        x = self.bn(
            x,
            training=training,
        )

        x = self.relu(x)

        return x


# ==========================================================
# Residual Block
# ==========================================================

class ResidualBlock(layers.Layer):

    def __init__(
        self,
        filters: int,
        stride: int = 1,
    ):

        super().__init__()

        self.filters = filters
        self.stride = stride

        self.conv1 = ConvBlock(
            filters=filters,
            strides=stride,
        )

        self.conv2 = layers.Conv2D(
            filters,
            kernel_size=3,
            padding="same",
            use_bias=False,
            kernel_initializer="he_normal",
        )

        self.bn2 = layers.BatchNormalization()

        self.relu = layers.ReLU()

        self.shortcut = None

    def build(self, input_shape):

        input_channels = input_shape[-1]

        if (
            self.stride != 1
            or input_channels != self.filters
        ):

            self.shortcut = tf.keras.Sequential(
                [
                    layers.Conv2D(
                        filters=self.filters,
                        kernel_size=1,
                        strides=self.stride,
                        use_bias=False,
                        kernel_initializer="he_normal",
                    ),
                    layers.BatchNormalization(),
                ]
            )

        super().build(input_shape)

    def call(
        self,
        inputs,
        training=False,
    ):

        residual = inputs

        x = self.conv1(
            inputs,
            training=training,
        )

        x = self.conv2(x)

        x = self.bn2(
            x,
            training=training,
        )

        if self.shortcut is not None:

            residual = self.shortcut(
                residual,
                training=training,
            )

        x = layers.add([x, residual])

        x = self.relu(x)

        return x


# ==========================================================
# Dense Block
# ==========================================================

class DenseBlock(layers.Layer):

    def __init__(
        self,
        units: int,
        dropout: float = 0.3,
    ):

        super().__init__()

        self.dense = layers.Dense(
            units,
            activation=None,
            kernel_initializer="he_normal",
        )

        self.bn = layers.BatchNormalization()

        self.relu = layers.ReLU()

        self.dropout = layers.Dropout(
            dropout,
        )

    def call(
        self,
        inputs,
        training=False,
    ):

        x = self.dense(inputs)

        x = self.bn(
            x,
            training=training,
        )

        x = self.relu(x)

        x = self.dropout(
            x,
            training=training,
        )

        return x