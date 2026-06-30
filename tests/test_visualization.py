from recognition.evaluator import (
    ConfusionMatrix,
    Visualization,
)


def main():

    y_true = [
        0, 1, 2,
        1, 0, 2,
        2, 1,
    ]

    y_pred = [
        0, 1, 2,
        0, 0, 2,
        1, 1,
    ]

    classes = [
        "fist",
        "okay",
        "peace",
    ]

    matrix = ConfusionMatrix.compute(
        y_true,
        y_pred,
    )

    Visualization.plot_confusion_matrix(
        matrix,
        classes,
        save_path="artifacts/confusion_matrix.png",
    )

    Visualization.plot_class_distribution(
        {
            "fist": 150,
            "okay": 200,
            "peace": 180,
        },
        save_path="artifacts/class_distribution.png",
    )

    print("Visualization tests passed.")


if __name__ == "__main__":

    main()