from recognition.config import (
    IMAGE_DIR,
    GESTURES,
)

from recognition.network import (
    GestureRecognitionModel,
)

from recognition.predictor import (
    ImageLoader,
    Predictor,
)


def main():

    image_path = next(

        (IMAGE_DIR / GESTURES[0]).glob("*.png")

    )

    image = ImageLoader.load(

        image_path,

    )

    model = GestureRecognitionModel.build_model(

        num_classes=len(GESTURES),

    )

    predictor = Predictor(

        model=model,

        class_names=GESTURES,

    )

    prediction = predictor.predict(

        image,

    )

    if prediction is None:

        print("No hand detected.")

        return

    print("Gesture:", prediction["gesture"])

    print("Confidence:", prediction["confidence"])

    print("Handedness:", prediction["handedness"])

    print("Bounding Box:", prediction["bounding_box"])

    print("Probabilities Shape:", prediction["probabilities"].shape)

    predictor.close()


if __name__ == "__main__":

    main()
    