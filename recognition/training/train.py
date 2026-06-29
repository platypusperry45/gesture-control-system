"""
Training entry point.

Run:

python -m recognition.training.train
"""

from __future__ import annotations

from recognition.dataset import (
    DatasetBuilder,
    DatasetSplitter,
    TensorFlowDatasetBuilder,
)

from recognition.network import (
    GestureRecognitionModel,
)

from recognition.training import (
    Trainer,
    TrainingConfig,
)


def main():

    print("=" * 60)
    print("Building dataset...")
    print("=" * 60)

    dataset = DatasetBuilder().build()

    splitter = DatasetSplitter()

    bundle = splitter.split(
        dataset,
    )

    print("=" * 60)
    print("Creating TensorFlow datasets...")
    print("=" * 60)

    tf_builder = TensorFlowDatasetBuilder()

    train_dataset = tf_builder.build(
        bundle.train,
        training=True,
    )

    validation_dataset = tf_builder.build(
        bundle.validation,
        training=False,
    )

    test_dataset = tf_builder.build(
        bundle.test,
        training=False,
    )

    print("=" * 60)
    print("Creating model...")
    print("=" * 60)

    model = GestureRecognitionModel.build_model(
        num_classes=len(dataset.label_encoder.classes_),
    )

    trainer = Trainer(
        training_config=TrainingConfig(),
    )

    print("=" * 60)
    print("Compiling model...")
    print("=" * 60)

    trainer.compile(
        model,
    )

    print("=" * 60)
    print("Starting training...")
    print("=" * 60)

    history = trainer.fit(

        model,

        train_dataset,

        validation_dataset,

    )

    print("=" * 60)
    print("Evaluating...")
    print("=" * 60)

    trainer.evaluate(
        model,
        test_dataset,
    )

    print("=" * 60)
    print("Saving final model...")
    print("=" * 60)

    trainer.save(

        model,

        "recognition/artifacts/trained_models/gesture_recognition.keras",

    )

    print("=" * 60)
    print("Training completed.")
    print("=" * 60)


if __name__ == "__main__":

    main()