from recognition.config import (
    IMAGE_DIR,
    GESTURES,
)

from recognition.predictor import (
    ImageLoader,
    HandDetector,
)


def main():

    image_path = next(

        (IMAGE_DIR / GESTURES[0]).glob("*.png")

    )

    image = ImageLoader.load(
        image_path,
    )

    detector = HandDetector()

    result = detector.detect(
        image,
    )

    if result is None:

        print("No hand detected.")

        return

    print(

        "Landmarks:",

        result.landmarks.shape,

    )

    print(

        "Handedness:",

        result.handedness,

    )

    print(

        "Bounding Box:",

        result.bbox,

    )


if __name__ == "__main__":

    main()