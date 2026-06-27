"""
Custom exceptions for the Vision Layer.
"""


class VisionLayerError(Exception):
    """
    Base exception for all Vision Layer errors.
    """


class CameraUnavailableError(VisionLayerError):
    """
    Raised when the webcam cannot be opened.
    """


class FrameReadError(VisionLayerError):
    """
    Raised when a frame cannot be read from the webcam.
    """


class DetectionError(VisionLayerError):
    """
    Raised when hand detection fails.
    """


class CropError(VisionLayerError):
    """
    Raised when hand crop generation fails.
    """


class PipelineError(VisionLayerError):
    """
    Raised when the vision pipeline encounters an unrecoverable error.
    """