import cv2

from recognition.config import (
    IMAGE_DIR,
    GESTURES,
)

from recognition.network import GestureRecognitionModel

from recognition.predictor import (
    ImageLoader,
    Predictor,
    Visualizer,
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

    hand = predictor.detector.detect(

        image,

    )

    visualizer = Visualizer()

    output = visualizer.draw(

        image.copy(),

        prediction,

        hand.landmarks,

    )

    cv2.imshow(

        "Prediction",

        cv2.cvtColor(

            output,

            cv2.COLOR_RGB2BGR,

        ),

    )

    cv2.waitKey(0)

    cv2.destroyAllWindows()

    predictor.close()


if __name__ == "__main__":

    main()