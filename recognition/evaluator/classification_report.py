"""
Classification Report.

Generates detailed evaluation reports
for gesture recognition models.
"""

from __future__ import annotations

import pandas as pd

from sklearn.metrics import classification_report


class ClassificationReport:
    """
    Utilities for generating classification reports.
    """

    # =====================================================
    # Dictionary Report
    # =====================================================

    @staticmethod
    def generate(
        y_true,
        y_pred,
        class_names,
    ) -> dict:

        """
        Returns the classification report
        as a Python dictionary.
        """

        return classification_report(

            y_true,

            y_pred,

            target_names=class_names,

            output_dict=True,

            zero_division=0,

        )

    # =====================================================
    # Text Report
    # =====================================================

    @staticmethod
    def to_text(
        y_true,
        y_pred,
        class_names,
    ) -> str:

        """
        Returns the classification report
        as formatted text.
        """

        return classification_report(

            y_true,

            y_pred,

            target_names=class_names,

            zero_division=0,

        )

    # =====================================================
    # DataFrame Report
    # =====================================================

    @staticmethod
    def to_dataframe(
        y_true,
        y_pred,
        class_names,
    ) -> pd.DataFrame:

        """
        Returns the classification report
        as a pandas DataFrame.
        """

        report = classification_report(

            y_true,

            y_pred,

            target_names=class_names,

            output_dict=True,

            zero_division=0,

        )

        return pd.DataFrame(
            report,
        ).transpose()