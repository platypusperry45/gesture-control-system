from pathlib import Path
from datetime import datetime

from fastapi import APIRouter

router = APIRouter(
    prefix="/dataset",
    tags=["Dataset"],
)

DATASET_DIR = (
    Path(__file__).resolve().parents[2]
    / "recognition"
    / "data"
    / "raw"
    / "images"
)


@router.get("/overview")
def dataset_overview():

    DATASET_DIR.mkdir(parents=True, exist_ok=True)

    classes = []

    total_images = 0

    latest = None

    for folder in DATASET_DIR.iterdir():

        if not folder.is_dir():
            continue

        classes.append(folder.name)

        images = list(folder.glob("*"))

        total_images += len(images)

        for img in images:

            t = img.stat().st_mtime

            if latest is None or t > latest:
                latest = t

    size = 0

    for f in DATASET_DIR.rglob("*"):

        if f.is_file():
            size += f.stat().st_size

    return {

        "name": "Gesture Dataset",

        "images": total_images,

        "classes": len(classes),

        "size": f"{size/1024/1024:.2f} MB",

        "updated":
            datetime.fromtimestamp(latest).strftime("%d %b %Y")
            if latest
            else "--",

        "path": str(DATASET_DIR),

        "completion": 100,

    }