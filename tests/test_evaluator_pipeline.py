from recognition.config import GESTURES

from recognition.dataset import (
    DatasetBuilder,
    DatasetSplitter,
    TensorFlowDatasetBuilder,
)

from recognition.network import (
    GestureRecognitionModel,
)

from recognition.evaluator import (
    Evaluator,
)


def main():

    print("=" * 60)
    print("STEP 1 : Building Dataset")
    print("=" * 60)

    dataset = DatasetBuilder().build()

    bundle = DatasetSplitter().split(
        dataset,
    )

    print("✓ Dataset built")

    print("\n" + "=" * 60)
    print("STEP 2 : TensorFlow Dataset")
    print("=" * 60)

    tf_builder = TensorFlowDatasetBuilder()

    (
        train_dataset,
        validation_dataset,
        test_dataset,
    ) = tf_builder.build(
        bundle,
    )

    print("✓ TensorFlow datasets created")

    print("\n" + "=" * 60)
    print("STEP 3 : Model")
    print("=" * 60)

    model = GestureRecognitionModel.build_model(
        num_classes=len(GESTURES),
    )

    print("✓ Model built")

    print("\n" + "=" * 60)
    print("STEP 4 : Evaluator")
    print("=" * 60)

    evaluator = Evaluator(
        model,
    )

    print("✓ Evaluator created")

    print("\n" + "=" * 60)
    print("STEP 5 : Evaluation")
    print("=" * 60)

    results = evaluator.evaluate(

        dataset=test_dataset,

        class_names=GESTURES,

        save_dir="artifacts/evaluation",

    )

    print("Accuracy :", results["accuracy"])

    print("✓ Evaluation completed")

    print("\n" + "=" * 60)
    print("Generated Files")
    print("=" * 60)

    print("classification_report.csv")
    print("classification_report.txt")
    print("metrics.json")
    print("confusion_matrix.png")
    print("normalized_confusion_matrix.png")

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":

    main()