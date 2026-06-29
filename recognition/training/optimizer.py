"""
Optimizer factory.

Creates optimizers used during model training.
"""

from __future__ import annotations

import tensorflow as tf

from .config import TrainingConfig


class OptimizerFactory:
    """
    Factory for constructing optimizers.
    """

    def __init__(
        self,
        config: TrainingConfig | None = None,
    ):

        self.config = (
            config
            if config is not None
            else TrainingConfig()
        )

    # =====================================================
    # AdamW
    # =====================================================

    def adamw(
        self,
    ) -> tf.keras.optimizers.Optimizer:

        return tf.keras.optimizers.AdamW(
            learning_rate=self.config.learning_rate,
            weight_decay=self.config.weight_decay,
            clipnorm=self.config.gradient_clip_norm,
            name="AdamW",
        )

    # =====================================================
    # Adam
    # =====================================================

    def adam(
        self,
    ) -> tf.keras.optimizers.Optimizer:

        return tf.keras.optimizers.Adam(
            learning_rate=self.config.learning_rate,
            clipnorm=self.config.gradient_clip_norm,
            name="Adam",
        )

    # =====================================================
    # Default
    # =====================================================

    def default(
        self,
    ) -> tf.keras.optimizers.Optimizer:

        return self.adamw()