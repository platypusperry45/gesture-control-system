"""
Dataset storage module.

Responsible for saving gesture samples to disk.

This module is independent of the camera, UI, and Vision Pipeline.
"""

from __future__ import annotations

import csv
import time

import cv2

from vision.models import HandData

from .config import (
    GESTURES,
    IMAGE_DIR,
    LANDMARK_DIR,
    METADATA_DIR,
)


class DatasetStorage:
    """
    Handles persistent storage of collected gesture samples.
    """

    def __init__(self):

        self._create_directories()

        self._initialize_csv_files()

        self._sample_indices = self._initialize_sample_indices()

    # ==========================================================
    # Directory Management
    # ==========================================================

    def _create_directories(self) -> None:
        """
        Create dataset directory structure.
        """

        IMAGE_DIR.mkdir(parents=True, exist_ok=True)
        LANDMARK_DIR.mkdir(parents=True, exist_ok=True)
        METADATA_DIR.mkdir(parents=True, exist_ok=True)

        for gesture in GESTURES:
            (IMAGE_DIR / gesture).mkdir(
                parents=True,
                exist_ok=True,
            )

    # ==========================================================
    # CSV Initialization
    # ==========================================================

    def _initialize_csv_files(self) -> None:

        self._initialize_landmark_csvs()

        self._initialize_metadata_csv()

    def _initialize_landmark_csvs(self) -> None:

        header = [
            "filename",
            "handedness",
        ]

        for i in range(21):
            header.extend(
                [
                    f"lm{i}_x",
                    f"lm{i}_y",
                    f"lm{i}_z",
                ]
            )

        for gesture in GESTURES:

            csv_path = LANDMARK_DIR / f"{gesture}.csv"

            if csv_path.exists():
                continue

            with open(
                csv_path,
                "w",
                newline="",
            ) as file:

                writer = csv.writer(file)

                writer.writerow(header)

    def _initialize_metadata_csv(self) -> None:

        csv_path = METADATA_DIR / "metadata.csv"

        if csv_path.exists():
            return

        with open(
            csv_path,
            "w",
            newline="",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "filename",
                    "gesture",
                    "handedness",
                    "timestamp",
                ]
            )

    # ==========================================================
    # Sample Index Management
    # ==========================================================

    def _initialize_sample_indices(self) -> dict[str, int]:
        """
        Scan dataset once and cache the next index
        for every gesture.
        """

        indices = {}

        for gesture in GESTURES:

            folder = IMAGE_DIR / gesture

            existing = [
                int(file.stem)
                for file in folder.glob("*.png")
                if file.stem.isdigit()
            ]

            indices[gesture] = max(existing, default=-1) + 1

        return indices

    def next_index(
        self,
        gesture: str,
    ) -> int:
        """
        Return next available index.
        """

        index = self._sample_indices[gesture]

        self._sample_indices[gesture] += 1

        return index

    # ==========================================================
    # Image Saving
    # ==========================================================

    def save_image(
        self,
        image,
        gesture: str,
        index: int,
    ) -> str:

        filename = f"{index:06d}.png"

        path = IMAGE_DIR / gesture / filename

        image_bgr = cv2.cvtColor(
            image,
            cv2.COLOR_RGB2BGR,
        )

        success = cv2.imwrite(
            str(path),
            image_bgr,
        )

        if not success:
            raise IOError(f"Unable to save image: {path}")

        return filename

    # ==========================================================
    # Landmark Saving
    # ==========================================================

    def save_landmarks(
        self,
        hand: HandData,
        gesture: str,
        filename: str,
    ) -> None:

        csv_path = LANDMARK_DIR / f"{gesture}.csv"

        row = [
            filename,
            hand.handedness,
        ]

        for landmark in hand.landmarks:

            row.extend(
                [
                    landmark.x,
                    landmark.y,
                    landmark.z,
                ]
            )

        with open(
            csv_path,
            "a",
            newline="",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(row)

    # ==========================================================
    # Metadata Saving
    # ==========================================================

    def save_metadata(
        self,
        hand: HandData,
        gesture: str,
        filename: str,
    ) -> None:

        csv_path = METADATA_DIR / "metadata.csv"

        writerow = [
            filename,
            gesture,
            hand.handedness,
            time.strftime("%Y-%m-%d %H:%M:%S"),
        ]

        with open(
            csv_path,
            "a",
            newline="",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(writerow)

    # ==========================================================
    # Public API
    # ==========================================================

    def save_sample(
        self,
        hand: HandData,
        gesture: str,
    ) -> str:
        """
        Save a complete gesture sample.

        Returns
        -------
        str
            Saved filename.
        """

        index = self.next_index(
            gesture,
        )

        filename = self.save_image(
            hand.cropped_image,
            gesture,
            index,
        )

        self.save_landmarks(
            hand,
            gesture,
            filename,
        )

        self.save_metadata(
            hand,
            gesture,
            filename,
        )

        return filename

    # ==========================================================
    # Dataset Statistics
    # ==========================================================

    def get_sample_count(
        self,
        gesture: str,
    ) -> int:
        """
        Number of saved samples for a gesture.
        """

        return self._sample_indices[gesture]

    def get_dataset_statistics(self) -> dict[str, int]:
        """
        Returns sample count for every gesture.
        """

        return {
            gesture: self.get_sample_count(gesture)
            for gesture in GESTURES
        }