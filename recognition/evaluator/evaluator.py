"""
Model Evaluator.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from .metrics import EvaluationMetrics
from .classification_report import ClassificationReport
from .confusion_matrix import ConfusionMatrix
from .visualization import Visualization


class Evaluator:
    """
    Evaluates a trained gesture recognition model.
    """

    def __init__(
        self,
        model,
    ):

        self.model = model

    # =====================================================
    # Collect Predictions
    # =====================================================

    def predict(
        self,
        dataset,
    ):

        y_true = []
        y_pred = []

        for inputs, labels in dataset:

            predictions = self.model(
                inputs,
                training=False,
            ).numpy()

            predictions = np.argmax(
                predictions,
                axis=1,
            )

            y_pred.extend(
                predictions.tolist()
            )

            y_true.extend(
                labels.numpy().tolist()
            )

        return (

            np.asarray(y_true),

            np.asarray(y_pred),

        )

    # =====================================================
    # Evaluation
    # =====================================================

    def evaluate(
        self,
        dataset,
        class_names,
        save_dir: str | Path | None = None,
    ) -> dict:

        y_true, y_pred = self.predict(
            dataset,
        )
        prediction_df = pd.DataFrame({
            "true_label": [class_names[i] for i in y_true],
            "predicted_label": [class_names[i] for i in y_pred],
            "correct": y_true == y_pred,
        })
        
        # ----------------------------
        # Accuracy
        # ----------------------------

        accuracy = float(
            np.mean(
                y_true == y_pred
            )
        )

        # ----------------------------
        # Classification Report
        # ----------------------------

        report_dict = (

            ClassificationReport.generate(

                y_true,

                y_pred,

                class_names,

            )

        )

        report_text = (

            ClassificationReport.to_text(

                y_true,

                y_pred,

                class_names,

            )

        )

        report_df = (

            ClassificationReport.to_dataframe(

                y_true,

                y_pred,

                class_names,

            )

        )

        # ----------------------------
        # Confusion Matrix
        # ----------------------------

        matrix = ConfusionMatrix.compute(

            y_true,

            y_pred,

            normalize=False,

        )

        normalized = ConfusionMatrix.compute(

            y_true,

            y_pred,

            normalize=True,

        )

        # ----------------------------
        # Save Results
        # ----------------------------

        if save_dir is not None:

            prediction_df.to_csv(
                save_dir / "predictions.csv",
                index=False,
            )
            
            save_dir = Path(save_dir)

            save_dir.mkdir(
                parents=True,
                exist_ok=True,
            )

            Visualization.plot_confusion_matrix(

                matrix,

                class_names,

                save_path=(
                    save_dir /
                    "confusion_matrix.png"
                ),

            )

            Visualization.plot_confusion_matrix(

                normalized,

                class_names,

                title="Normalized Confusion Matrix",

                save_path=(
                    save_dir /
                    "normalized_confusion_matrix.png"
                ),

            )

            report_df.to_csv(

                save_dir /
                "classification_report.csv",

            )

            with open(

                save_dir /
                "classification_report.txt",

                "w",

                encoding="utf-8",

            ) as file:

                file.write(
                    report_text
                )

            metrics = {
                "accuracy": accuracy,
                "precision_macro": report_dict["macro avg"]["precision"],
                "recall_macro": report_dict["macro avg"]["recall"],
                "f1_macro": report_dict["macro avg"]["f1-score"],
                "precision_weighted": report_dict["weighted avg"]["precision"],
                "recall_weighted": report_dict["weighted avg"]["recall"],
                "f1_weighted": report_dict["weighted avg"]["f1-score"],
            }

            with open(
                save_dir / "metrics.json",
                "w",
                encoding="utf-8",
            ) as file:

                json.dump(
                    metrics,
                    file,
                    indent=4,
                )


        print("\n" + "=" * 50)
        print("Evaluation Summary")
        print("=" * 50)

        print(f"Accuracy            : {accuracy:.2%}")
        print(f"Macro Precision     : {metrics['precision_macro']:.2%}")
        print(f"Macro Recall        : {metrics['recall_macro']:.2%}")
        print(f"Macro F1 Score      : {metrics['f1_macro']:.2%}")

        if save_dir is not None:
            print(f"\nResults saved to: {save_dir}")

        print("=" * 50 + "\n")  

        # ----------------------------
        # Return Everything
        # ----------------------------

        return {

            "accuracy": accuracy,

            "classification_report": report_dict,

            "confusion_matrix": matrix,

            "normalized_confusion_matrix": normalized,

        }