"""
Training entry point.

Run:

python -m recognition.training.train
"""

from __future__ import annotations

import os
from collections import Counter

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from backend.training_callback import BackendTrainingCallback

from recognition.dataset import (
    DatasetBuilder,
    DatasetSplitter,
    TensorFlowDatasetBuilder,
)

from recognition.network import GestureRecognitionModel

from recognition.training import (
    Trainer,
    TrainingConfig,
)


def main(training):

    try:

        training.start()

        print("=" * 60)
        print("Building dataset...")
        print("=" * 60)

        dataset_builder = DatasetBuilder()
        dataset = dataset_builder.build()

        training.dataset_size = len(dataset.samples)
        training.num_classes = len(dataset_builder.label_encoder.classes_)
        training.class_names = list(dataset_builder.label_encoder.classes_)

        print("\n================ LABEL ORDER (TRAINING) ================\n")
        print(dataset_builder.label_encoder.classes_)
        print("Num classes:", len(dataset_builder.label_encoder.classes_))
        print("========================================================\n")

        counts = Counter(sample.gesture for sample in dataset.samples)

        print("=" * 60)
        print("DATASET DEBUG")
        print("=" * 60)
        print(counts)
        print()
        print("Number of classes:", len(counts))
        print("Classes:", sorted(counts.keys()))

        training.add_log(
            f"Loaded dataset with {len(dataset.samples)} images across {len(counts)} classes."
        )

        print("=" * 60)
        print("Splitting dataset...")
        print("=" * 60)

        splitter = DatasetSplitter()
        bundle = splitter.split(dataset)

        print("=" * 60)
        print("Creating TensorFlow datasets...")
        print("=" * 60)

        tf_builder = TensorFlowDatasetBuilder(
            batch_size=32,
            cache=True,
        )

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
            num_classes=len(dataset_builder.label_encoder.classes_)
        )

        trainer = Trainer(
            training_config=TrainingConfig(),
        )

        print("=" * 60)
        print("Compiling model...")
        print("=" * 60)

        trainer.compile(model)

        print("=" * 60)
        print("Starting training...")
        print("=" * 60)

        training.add_log("Training started.")

        callback = BackendTrainingCallback(training)

        history = trainer.fit(
            model,
            train_dataset,
            validation_dataset,
            extra_callbacks=[callback],
        )

        print("=" * 60)
        print("Evaluating model...")
        print("=" * 60)

        metrics = trainer.evaluate(
            model,
            test_dataset,
        )

        print("\nTest Results")
        print("-" * 40)
        print(f"Loss: {metrics['loss']:.4f}")
        print(f"Accuracy: {metrics['accuracy']:.4f}")

        if "top3_accuracy" in metrics:
            print(f"Top-3 Accuracy: {metrics['top3_accuracy']:.4f}")

        training.test_loss = float(metrics["loss"])
        training.test_accuracy = float(metrics["accuracy"])

        if "top3_accuracy" in metrics:
            training.test_top3_accuracy = float(
                metrics["top3_accuracy"]
            )

        training.add_log(
            f"Test Accuracy: {metrics['accuracy']*100:.2f}%"
        )

        if "top3_accuracy" in metrics:
            training.add_log(
                f"Top-3 Accuracy: {metrics['top3_accuracy']*100:.2f}%"
            )

        # ----------------------------------------
        # Save epoch history for frontend charts
        # ----------------------------------------

        if history.history:

            epochs = len(history.history["loss"])

            for i in range(epochs):

                training.history.append(

                    {
                        "epoch": i + 1,
                        "loss": float(history.history["loss"][i]),
                        "accuracy": float(history.history["accuracy"][i]),
                        "val_loss": float(history.history["val_loss"][i]),
                        "val_accuracy": float(history.history["val_accuracy"][i]),
                    }

                )

        print("=" * 60)
        print("Saving model...")
        print("=" * 60)

        trainer.save(
            model,
            "recognition/artifacts/trained_models/gesture_recognition.h5",
        )

        training.add_log("Model saved successfully.")

        training.finish()

        print("=" * 60)
        print("Training completed successfully.")
        print("=" * 60)

    except Exception as e:

        training.running = False
        training.completed = False
        training.error = str(e)

        training.add_log(
            f"ERROR: {e}",
            level="ERROR",
        )

        raise


if __name__ == "__main__":

    from backend.training_manager import TrainingManager

    training = TrainingManager()

    main(training)