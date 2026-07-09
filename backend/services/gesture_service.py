from pathlib import Path


class GestureService:

    def __init__(self):

        self.dataset_dir = (
            Path(__file__).resolve().parents[2]
            / "recognition"
            / "data"
            / "raw"
            / "images"
        )

    def dataset_summary(self):

        self.dataset_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        classes = []

        total_images = 0

        for folder in self.dataset_dir.iterdir():

            if not folder.is_dir():
                continue

            count = len(
                [
                    x
                    for x in folder.iterdir()
                    if x.suffix.lower()
                    in [
                        ".jpg",
                        ".jpeg",
                        ".png",
                    ]
                ]
            )

            total_images += count

            classes.append(
                {
                    "name": folder.name,
                    "images": count,
                }
            )

        size_mb = 0

        for file in self.dataset_dir.rglob("*"):

            if file.is_file():

                size_mb += file.stat().st_size

        size_mb /= 1024 * 1024

        return {

            "name": "Gesture Dataset",

            "images": total_images,

            "classes": len(classes),

            "class_list": classes,

            "size": f"{size_mb:.1f} MB",

            "path": str(self.dataset_dir),

            "completion": 100,

        }


gesture_service = GestureService()