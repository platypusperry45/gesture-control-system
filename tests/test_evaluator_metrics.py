from recognition.evaluator import EvaluationMetrics


def main():

    metrics = EvaluationMetrics.build()

    print(metrics)


if __name__ == "__main__":

    main()