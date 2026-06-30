from recognition.evaluator import ConfusionMatrix


def main():

    y_true = [

        0,
        1,
        2,
        1,
        0,
        2,
        2,
        1,
    ]

    y_pred = [

        0,
        1,
        2,
        0,
        0,
        2,
        1,
        1,
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

    print(matrix)

    ConfusionMatrix.plot(
        matrix,
        classes,
        save_path="artifacts/confusion_matrix.png",
    )

    print("✓ Confusion matrix saved")


if __name__ == "__main__":

    main()