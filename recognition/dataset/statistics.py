"""
Dataset statistics and reporting utilities.
"""

from __future__ import annotations

from collections import Counter

from .models import (
    Dataset,
    DatasetBundle,
    DatasetSplit,
)


class DatasetStatistics:
    """
    Computes statistics for datasets.
    """

    # =====================================================
    # Dataset
    # =====================================================

    @staticmethod
    def dataset_summary(
        dataset: Dataset,
    ) -> dict:

        counts = Counter()

        for sample in dataset.samples:

            counts[sample.gesture] += 1

        total = len(dataset)

        return {

            "total": total,

            "classes": len(counts),

            "counts": dict(counts),

            "min": min(counts.values())
            if counts else 0,

            "max": max(counts.values())
            if counts else 0,

            "mean": (
                total / len(counts)
                if counts else 0
            ),

        }

    # =====================================================
    # Dataset Split
    # =====================================================

    @staticmethod
    def split_summary(
        split: DatasetSplit,
    ) -> dict:

        counts = Counter()

        for sample in split.samples:

            counts[sample.gesture] += 1

        return {

            "name": split.name,

            "size": len(split),

            "counts": dict(counts),

        }

    # =====================================================
    # Dataset Bundle
    # =====================================================

    @classmethod
    def bundle_summary(
        cls,
        bundle: DatasetBundle,
    ) -> dict:

        return {

            "train":
                cls.split_summary(
                    bundle.train
                ),

            "validation":
                cls.split_summary(
                    bundle.validation
                ),

            "test":
                cls.split_summary(
                    bundle.test
                ),

            "total":

                len(bundle.train)

                + len(bundle.validation)

                + len(bundle.test),

        }

    # =====================================================
    # Pretty Print
    # =====================================================

    @classmethod
    def print_summary(
        cls,
        bundle: DatasetBundle,
    ):

        summary = cls.bundle_summary(
            bundle
        )

        print()

        print("=" * 50)

        print("DATASET SUMMARY")

        print("=" * 50)

        print()

        print(
            f"Total Samples : {summary['total']}"
        )

        print()

        for name in (

            "train",

            "validation",

            "test",

        ):

            split = summary[name]

            print(

                f"{split['name'].capitalize():12}"

                f": {split['size']}"

            )

        print()

        print("-" * 50)

        print("TRAIN CLASS DISTRIBUTION")

        print("-" * 50)

        for gesture, count in sorted(

            summary["train"][
                "counts"
            ].items()

        ):

            print(

                f"{gesture:20}"

                f"{count}"

            )

        print()

        print("=" * 50)

        print()