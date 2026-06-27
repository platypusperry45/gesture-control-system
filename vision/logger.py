"""
Logging configuration for the Vision Layer.
"""

import logging
import sys
from pathlib import Path


LOG_FORMAT = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
)


def get_logger(name: str = "vision") -> logging.Logger:
    """
    Returns a configured logger instance.

    Args:
        name:
            Name of the logger.

    Returns:
        Configured logger.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(LOG_FORMAT)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    logger.propagate = False

    return logger


logger = get_logger()