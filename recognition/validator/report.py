"""
Pretty console reporting for the Dataset Validator.
"""

from __future__ import annotations

from .models import ValidationReport
from .utils import pretty


class ReportPrinter:

    @staticmethod
    def print(report: ValidationReport):

        print()
        print("=" * 60)
        print("DATASET VALIDATION REPORT")
        print("=" * 60)

        print(f"Dataset : {report.dataset_root}")

        print()

        print("-" * 60)
        print("CLASS DISTRIBUTION")
        print("-" * 60)

        for cls in report.classes:

            print(
                f"{cls.gesture:<15}"
                f"Images: {pretty(cls.image_count):>6}"
                f"   "
                f"Landmarks: {pretty(cls.landmark_rows):>6}"
            )

        print()

        print("-" * 60)
        print("SUMMARY")
        print("-" * 60)

        print(f"Images               : {pretty(report.total_images)}")
        print(f"Landmark Rows        : {pretty(report.total_landmark_rows)}")
        print(f"Metadata Rows        : {pretty(report.total_metadata_rows)}")
        print(f"Corrupted Images     : {pretty(report.corrupted_images)}")
        print(f"Missing Landmark CSV : {pretty(report.missing_landmark_files)}")
        print(f"Stale Metadata Rows  : {pretty(report.stale_metadata_rows)}")

        print()

        if report.issues:

            print("-" * 60)
            print("ISSUES")
            print("-" * 60)

            for issue in report.issues:

                print(
                    f"[{issue.severity}] {issue.message}"
                )

        else:

            print("No issues found.")

        print()

        print("=" * 60)

        if report.passed:

            print("✓ DATASET VALIDATION PASSED")

        else:

            print("✗ DATASET VALIDATION FAILED")

        print("=" * 60)