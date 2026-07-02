"""
Training entry point.

Run:

python -m recognition.training.train
"""

from __future__ import annotations
import os


os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
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

from collections import Counter


def main():

    print("=" * 60)
    print("Building dataset...")
    print("=" * 60)

    dataset_builder = DatasetBuilder()
    dataset = dataset_builder.build()
    print("\n================ LABEL ORDER (TRAINING) ================\n")
    print(dataset_builder.label_encoder.classes_)
    print("Num classes:", len(dataset_builder.label_encoder.classes_))
    print("========================================================\n")

    print("=" * 60)
    print("DATASET DEBUG")
    print("=" * 60)

    counts = Counter(sample.gesture for sample in dataset.samples)

    print(counts)

    print()

    print("Number of classes:", len(counts))
    print("Classes:", sorted(counts.keys()))
   
    print("=" * 60)

    splitter = DatasetSplitter()

    bundle = splitter.split(
        dataset,
    )

    print("=" * 60)
    print("Creating TensorFlow datasets...")
    print("=" * 60)

    tf_builder = TensorFlowDatasetBuilder(
        batch_size=8,
        cache=False,
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
        num_classes = len(dataset_builder.label_encoder.classes_),
    )
    
    class_names = dataset_builder.label_encoder.classes_

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

        "recognition/artifacts/trained_models/gesture_recognition.h5",

    )

    print("=" * 60)
    print("Training completed.")
    print("=" * 60)


if __name__ == "__main__":

    main()