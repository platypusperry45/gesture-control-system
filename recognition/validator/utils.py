"""
Utility functions for the Dataset Validator.
"""

from __future__ import annotations

import csv
from pathlib import Path

from PIL import Image


# ----------------------------------------------------------
# Supported Image Extensions
# ----------------------------------------------------------

IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
}


# ----------------------------------------------------------
# Image File Check
# ----------------------------------------------------------

def is_image_file(path: Path) -> bool:
    """
    Returns True if the file is a supported image.
    """

    return path.suffix.lower() in IMAGE_EXTENSIONS


# ----------------------------------------------------------
# List Images
# ----------------------------------------------------------

def list_images(folder: Path) -> list[Path]:
    """
    Returns every image inside a folder.
    """

    if not folder.exists():
        return []

    images = []

    for file in folder.iterdir():

        if file.is_file() and is_image_file(file):

            images.append(file)

    return sorted(images)


# ----------------------------------------------------------
# Count CSV Rows
# ----------------------------------------------------------

def count_csv_rows(path: Path) -> int:
    """
    Counts CSV rows excluding the header.
    """

    if not path.exists():
        return 0

    with open(path, newline="", encoding="utf-8") as f:

        reader = csv.reader(f)

        # Skip header
        next(reader, None)

        return sum(1 for _ in reader)


# ----------------------------------------------------------
# Verify Image
# ----------------------------------------------------------

def verify_image(path: Path) -> tuple[bool, str]:
    """
    Verifies an image using Pillow.

    Returns
    -------
    (success, reason)
    """

    try:

        with Image.open(path) as img:

            img.verify()

        return True, ""

    except Exception as exc:

        return False, str(exc)


# ----------------------------------------------------------
# Folder Exists
# ----------------------------------------------------------

def folder_exists(path: Path) -> bool:
    """
    Safe folder existence check.
    """

    return path.exists() and path.is_dir()


# ----------------------------------------------------------
# File Exists
# ----------------------------------------------------------

def file_exists(path: Path) -> bool:
    """
    Safe file existence check.
    """

    return path.exists() and path.is_file()


# ----------------------------------------------------------
# Pretty Number
# ----------------------------------------------------------

def pretty(number: int) -> str:
    """
    Formats integers with commas.
    """

    return f"{number:,}"