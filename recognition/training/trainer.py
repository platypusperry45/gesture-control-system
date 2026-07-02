"""
Model trainer.

Coordinates model compilation, training, evaluation,
and model saving.
"""

from __future__ import annotations

from pathlib import Path

import tensorflow as tf

from .callbacks import CallbackFactory
from .losses import LossFactory
from .metrics import MetricsFactory
from .optimizer import OptimizerFactory
from .scheduler import SchedulerFactory
from .config import (
    TrainingConfig,
    SchedulerConfig,
    CheckpointConfig,
    EarlyStoppingConfig,
)


class Trainer:
    """
    High-level training interface.
    """

    def __init__(
        self,
        training_config: TrainingConfig | None = None,
        scheduler_config: SchedulerConfig | None = None,
        checkpoint_config: CheckpointConfig | None = None,
        early_stopping_config: EarlyStoppingConfig | None = None,
        checkpoint_dir: str | Path = (
            "recognition/artifacts/checkpoints"
        ),
        log_dir: str | Path = (
            "logs"
        ),
    ):

        self.training_config = (
            training_config
            if training_config is not None
            else TrainingConfig()
        )

        self.scheduler_config = (
            scheduler_config
            if scheduler_config is not None
            else SchedulerConfig()
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

        self.checkpoint_dir = Path(
            checkpoint_dir,
        )

        self.log_dir = Path(
            log_dir,
        )

    # =====================================================
    # Compile
    # =====================================================

    def compile(
        self,
        model: tf.keras.Model,
    ) -> None:

        optimizer = OptimizerFactory(
            self.training_config,
        ).default()

        loss = LossFactory.default()

        metrics = MetricsFactory.default()

        model.compile(

            optimizer=optimizer,

            loss=loss,

            metrics=metrics,

        )

    # =====================================================
    # Train
    # =====================================================

    def fit(
        self,
        model: tf.keras.Model,
        train_dataset: tf.data.Dataset,
        validation_dataset: tf.data.Dataset,
    ) -> tf.keras.callbacks.History:

        scheduler = SchedulerFactory(
            self.scheduler_config,
        ).default()

        callbacks = CallbackFactory(

            checkpoint_dir=self.checkpoint_dir,

            checkpoint_config=self.checkpoint_config,

            early_stopping_config=self.early_stopping_config,

        ).default(

            log_dir=self.log_dir,

            scheduler=scheduler,

        )

        history = model.fit(

            train_dataset,

            validation_data=validation_dataset,

            epochs=self.training_config.epochs,

            callbacks=callbacks,

            verbose=1,

        )

        return history

    # =====================================================
    # Evaluate
    # =====================================================

    def evaluate(
        self,
        model: tf.keras.Model,
        test_dataset: tf.data.Dataset,
    ):

        return model.evaluate(

            test_dataset,

            verbose=1,

        )

    # =====================================================
    # Predict
    # =====================================================

    def predict(
        self,
        model: tf.keras.Model,
        dataset: tf.data.Dataset,
    ):

        return model.predict(

            dataset,

            verbose=1,

        )

    # =====================================================
    # Save
    # =====================================================


    def save(self, model, path):

        path = Path(path)

        path.parent.mkdir(parents=True, exist_ok=True)

        weights_path = path.with_suffix(".weights.h5")

        model.save_weights(weights_path)

        print(f"Model weights saved to {weights_path}")