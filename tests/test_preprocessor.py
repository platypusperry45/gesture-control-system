from recognition.config import (
    IMAGE_DIR,
    GESTURES,
)

from recognition.predictor import (
    ImageLoader,
    HandDetector,
    Preprocessor,
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

    preprocessor = Preprocessor()

    inputs = preprocessor.preprocess(

        image,

        result.landmarks,
 
    )

    print(

        "Image Tensor Shape:",

        inputs["image"].shape,

    )

    print(

        "Landmark Tensor Shape:",

        inputs["landmarks"].shape,

    )


if __name__ == "__main__":

    main()