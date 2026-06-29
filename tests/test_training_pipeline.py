"""
Integration test for the complete training pipeline.

This test verifies:

1. Dataset builds correctly
2. Dataset splits correctly
3. TensorFlow datasets are created
4. Model builds
5. Model compiles
6. One training batch executes successfully
7. Evaluation executes successfully

This is NOT a full training run.
"""

from recognition.dataset import (
    DatasetBuilder,
    DatasetSplitter,
    TensorFlowDatasetBuilder,
)

from recognition.config import GESTURES

from recognition.network import (
    GestureRecognitionModel,
)

from recognition.training import (
    Trainer,
    TrainingConfig,
)


def main():

    print("=" * 60)
    print("STEP 1 : Building dataset")
    print("=" * 60)

    dataset = DatasetBuilder().build()

    splitter = DatasetSplitter()

    bundle = splitter.split(dataset)

    print("✓ Dataset built")

    print("\n" + "=" * 60)
    print("STEP 2 : TensorFlow datasets")
    print("=" * 60)

    tf_builder = TensorFlowDatasetBuilder()

    train_dataset, validation_dataset, test_dataset = (
        tf_builder.build(bundle)
    )

    print("✓ TF datasets created")

    print("\n" + "=" * 60)
    print("STEP 3 : Model")
    print("=" * 60)

    model = GestureRecognitionModel.build_model(
        num_classes=len(GESTURES),
    )

    print("✓ Model built")

    trainer = Trainer(
        training_config=TrainingConfig(
            epochs=1,
        )
    )

    trainer.compile(model)

    print("✓ Model compiled")

    print("\n" + "=" * 60)
    print("STEP 4 : One training batch")
    print("=" * 60)

    history = model.fit(

        train_dataset,

        validation_data=validation_dataset,

        epochs=1,

        steps_per_epoch=1,

        validation_steps=1,

        verbose=1,

    )

    print("✓ Training batch successful")

    print("\n" + "=" * 60)
    print("STEP 5 : One evaluation batch")
    print("=" * 60)

    model.evaluate(

        test_dataset,

        steps=1,

        verbose=1,

    )

    print("✓ Evaluation successful")

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":

    main()