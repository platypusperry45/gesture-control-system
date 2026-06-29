"""
Loss functions used during training.
"""

from __future__ import annotations

import tensorflow as tf


class LossFactory:
    """
    Factory for creating training losses.
    """

    @staticmethod
    def sparse_categorical_crossentropy(
        from_logits: bool = False,
    ) -> tf.keras.losses.Loss:

        return tf.keras.losses.SparseCategoricalCrossentropy(
            from_logits=from_logits,
            name="sparse_categorical_crossentropy",
        )

    @staticmethod
    def default() -> tf.keras.losses.Loss:

        return LossFactory.sparse_categorical_crossentropy()