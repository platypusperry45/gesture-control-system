from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

IMAGE_DIR = RAW_DATA_DIR / "images"

LANDMARK_DIR = RAW_DATA_DIR / "landmarks"

METADATA_DIR = RAW_DATA_DIR / "metadata"

COLLECTION_FPS = 10

COUNTDOWN_SECONDS = 3

TARGET_SAMPLES_PER_GESTURE = 300

SHOW_HAND_CROP = True

SHOW_FPS = True

SHOW_CONFIDENCE = True

SHOW_PROGRESS_BAR = True

SHOW_STATUS = True

AUTO_SWITCH_GESTURE = True

AUTO_CAPTURE_FPS = 8

SAMPLES_PER_SESSION = 30

WINDOW_NAME = "Gesture Dataset Collector"

CROP_WINDOW_NAME = "Hand Crop"

# ---------------------------------------------------------
# Quality Filter
# ---------------------------------------------------------

MIN_CONFIDENCE = 0.60

MIN_HAND_WIDTH = 70

MIN_HAND_HEIGHT = 70

MIN_CROP_SIZE = 96

ALLOW_BORDER_TOUCH = True

GESTURES = [
    "open_palm",
    "fist",
    "peace",
    "thumbs_up",
    "point",
    "okay",
]