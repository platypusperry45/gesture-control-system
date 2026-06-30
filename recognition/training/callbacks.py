"""
Training callback factory.
"""

from __future__ import annotations

from pathlib import Path

import tensorflow as tf

from .config import (
    CheckpointConfig,
    EarlyStoppingConfig,
)


class CallbackFactory:
    """
    Factory for Keras callbacks.
    """

    def __init__(
        self,
        checkpoint_dir: str | Path,
        checkpoint_config: CheckpointConfig | None = None,
        early_stopping_config: EarlyStoppingConfig | None = None,
    ):

        self.checkpoint_dir = Path(
            checkpoint_dir,
        )

        self.checkpoint_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.checkpoint_config = (
            checkpoint_config
            if checkpoint_config is not None
            else CheckpointConfig()
        )

        self.early_stopping_config = (
            early_stopping_config
            if early_stopping_config is not None
            else EarlyStoppingConfig()
        )

    # =====================================================
    # Model Checkpoint
    # =====================================================

    def checkpoint(
        self,
    ) -> tf.keras.callbacks.ModelCheckpoint:

        return tf.keras.callbacks.ModelCheckpoint(

            filepath=str(
                self.checkpoint_dir /
                "best.weights.h5"
            ),

            monitor=self.checkpoint_config.monitor,

            mode=self.checkpoint_config.mode,

            save_best_only=self.checkpoint_config.save_best_only,

            save_weights_only=True,

            verbose=1,

        )

    # =====================================================
    # Early Stopping
    # =====================================================

    def early_stopping(
        self,
    ) -> tf.keras.callbacks.EarlyStopping:

        return tf.keras.callbacks.EarlyStopping(

            monitor=self.early_stopping_config.monitor,

            patience=self.early_stopping_config.patience,

            restore_best_weights=self.early_stopping_config.restore_best_weights,

            verbose=1,

        )

    # =====================================================
    # TensorBoard
    # =====================================================

    def tensorboard(
        self,
        log_dir: str | Path,
    ) -> tf.keras.callbacks.TensorBoard:

        return tf.keras.callbacks.TensorBoard(

            log_dir=str(log_dir),

            histogram_freq=1,

            write_graph=True,

            write_images=False,

        )

    # =====================================================
    # CSV Logger
    # =====================================================

    def csv_logger(
        self,
    ) -> tf.keras.callbacks.CSVLogger:

        return tf.keras.callbacks.CSVLogger(

            filename=str(
                self.checkpoint_dir /
                "training_log.csv"
            ),

            append=False,

        )

    # =====================================================
    # Default Callback List
    # =====================================================

    def default(
        self,
        log_dir: str | Path,
        scheduler: tf.keras.callbacks.Callback,
    ) -> list[tf.keras.callbacks.Callback]:

        return [

            self.checkpoint(),

            self.early_stopping(),

            scheduler,

            self.tensorboard(
                log_dir,
            ),

            self.csv_logger(),

        ]