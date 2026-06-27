"""
Frame preprocessing module.

This module is responsible for preparing raw camera frames before
they enter the hand detection pipeline.

Responsibilities:
- Validate incoming frames
- Mirror frames (optional)
- Convert BGR images to RGB

Author: Akshat Yadav
Project: Gesture-Based Desktop Control System
"""

from __future__ import annotations

import cv2
import numpy as np


def validate_frame(frame: np.ndarray) -> None:
    """
    Validate an incoming image frame.

    Parameters
    ----------
    frame : np.ndarray
        Input image.

    Raises
    ------
    ValueError
        If frame is None or empty.
    TypeError
        If frame is not a numpy array.
    """

    if frame is None:
        raise ValueError("Frame is None.")

    if not isinstance(frame, np.ndarray):
        raise TypeError("Frame must be a numpy.ndarray.")

    if frame.size == 0:
        raise ValueError("Frame is empty.")


def mirror_frame(frame: np.ndarray) -> np.ndarray:
    """
    Horizontally flip the frame.

    Creates a natural mirror effect for webcam interaction.

    Parameters
    ----------
    frame : np.ndarray

    Returns
    -------
    np.ndarray
        Mirrored frame.
    """

    validate_frame(frame)

    return cv2.flip(frame, 1)


def convert_bgr_to_rgb(frame: np.ndarray) -> np.ndarray:
    """
    Convert OpenCV BGR image to RGB.

    MediaPipe expects RGB images.

    Parameters
    ----------
    frame : np.ndarray

    Returns
    -------
    np.ndarray
        RGB image.
    """

    validate_frame(frame)

    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)