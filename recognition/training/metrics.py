"""
Training metrics.
"""

from __future__ import annotations

import tensorflow as tf


class MetricsFactory:
    """
    Factory for commonly used training metrics.
    """

    @staticmethod
    def accuracy():

        return tf.keras.metrics.SparseCategoricalAccuracy(
            name="accuracy",
        )

    @staticmethod
    def top3():

        return tf.keras.metrics.SparseTopKCategoricalAccuracy(
            k=3,
            name="top3_accuracy",
        )

    @staticmethod
    def default():

        return [
            MetricsFactory.accuracy(),
            MetricsFactory.top3(),
        ]