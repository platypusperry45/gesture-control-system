"""
Learning rate scheduler factory.
"""

from __future__ import annotations

import tensorflow as tf

from .config import SchedulerConfig


class SchedulerFactory:
    """
    Factory for learning rate schedulers.
    """

    def __init__(
        self,
        config: SchedulerConfig | None = None,
    ):

        self.config = (
            config
            if config is not None
            else SchedulerConfig()
        )

    # =====================================================
    # Reduce LR on Plateau
    # =====================================================

    def reduce_on_plateau(
        self,
    ) -> tf.keras.callbacks.ReduceLROnPlateau:

        return tf.keras.callbacks.ReduceLROnPlateau(

            monitor="val_loss",

            factor=self.config.factor,

            patience=self.config.patience,

            min_lr=self.config.min_learning_rate,

            verbose=1,

        )

    # =====================================================
    # Default Scheduler
    # =====================================================

    def default(
        self,
    ) -> tf.keras.callbacks.Callback:

        return self.reduce_on_plateau()