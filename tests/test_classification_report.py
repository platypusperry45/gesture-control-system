from recognition.evaluator import ClassificationReport


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

    # Text Report
    print(

        ClassificationReport.to_text(

            y_true,

            y_pred,

            classes,

        )

    )

    # DataFrame Report
    print("\nDataFrame Report:\n")

    print(

        ClassificationReport.to_dataframe(

            y_true,

            y_pred,

            classes,

        )

    )

if __name__ == "__main__":

    main()