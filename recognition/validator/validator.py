"""
Dataset Validator.

Scans the raw dataset and generates a ValidationReport.
"""

from __future__ import annotations

from pathlib import Path

from recognition.config import (
    GESTURES,
    IMAGE_DIR,
    LANDMARK_DIR,
    METADATA_DIR,
)

from .models import ValidationReport
from .utils import (
    count_csv_rows,
    file_exists,
    folder_exists,
    list_images,
    verify_image,
)


class DatasetValidator:

    """
    Dataset validation engine.
    """

    def __init__(self):

        self.report = ValidationReport(
            dataset_root=IMAGE_DIR.parent,
        )

    # =====================================================
    # PUBLIC API
    # =====================================================

    def validate(self) -> ValidationReport:

        self._check_dataset_structure()

        self._scan_images()

        self._scan_landmarks()

        self._scan_metadata()

        return self.report

    # =====================================================
    # DATASET STRUCTURE
    # =====================================================

    def _check_dataset_structure(self):

        if not folder_exists(IMAGE_DIR):

            self.report.add_issue(
                "ERROR",
                "Images folder missing.",
                IMAGE_DIR,
            )

        if not folder_exists(LANDMARK_DIR):

            self.report.add_issue(
                "ERROR",
                "Landmarks folder missing.",
                LANDMARK_DIR,
            )

        if not folder_exists(METADATA_DIR):

            self.report.add_issue(
                "ERROR",
                "Metadata folder missing.",
                METADATA_DIR,
            )

    # =====================================================
    # IMAGE SCAN
    # =====================================================

    def _scan_images(self):

        for gesture in GESTURES:

            stats = self.report.add_class(gesture)

            folder = IMAGE_DIR / gesture

            if not folder_exists(folder):

                self.report.add_issue(
                    "ERROR",
                    f"Gesture folder missing: {gesture}",
                    folder,
                )

                continue

            images = list_images(folder)

            stats.image_count = len(images)

            self.report.total_images += len(images)

            for image in images:

                success, reason = verify_image(image)

                if success:

                    continue

                self.report.corrupted_images += 1

                self.report.add_issue(
                    "ERROR",
                    f"Corrupted image: {image.name} ({reason})",
                    image,
                )

    # =====================================================
    # LANDMARKS
    # =====================================================

    def _scan_landmarks(self):

        class_lookup = {
            cls.gesture: cls
            for cls in self.report.classes
        }

        for gesture in GESTURES:

            csv_path = LANDMARK_DIR / f"{gesture}.csv"

            if not file_exists(csv_path):

                self.report.missing_landmark_files += 1

                self.report.add_issue(
                    "ERROR",
                    f"Missing landmark CSV: {gesture}.csv",
                    csv_path,
                )

                continue

            rows = count_csv_rows(csv_path)

            self.report.total_landmark_rows += rows

            class_lookup[gesture].landmark_rows = rows

            if rows != class_lookup[gesture].image_count:

                self.report.add_issue(
                    "WARNING",
                    (
                        f"{gesture}: "
                        f"{rows} landmark rows, "
                        f"{class_lookup[gesture].image_count} images."
                    ),
                    csv_path,
                )

    # =====================================================
    # METADATA
    # =====================================================

    def _scan_metadata(self):

        metadata = METADATA_DIR / "metadata.csv"

        if not file_exists(metadata):

            self.report.missing_metadata = True

            self.report.add_issue(
                "WARNING",
                "metadata.csv not found.",
                metadata,
            )

            return

        rows = count_csv_rows(metadata)

        self.report.total_metadata_rows = rows

        stale = rows - self.report.total_images

        if stale > 0:

            self.report.stale_metadata_rows = stale

            self.report.add_issue(
                "WARNING",
                (
                    f"{stale} stale metadata rows "
                    "(likely deleted images)."
                ),
                metadata,
            )