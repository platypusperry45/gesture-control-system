from recognition.config import IMAGE_DIR
from recognition.config import GESTURES

from recognition.predictor import ImageLoader


def main():

    gesture = GESTURES[0]

    image_path = next(

        (IMAGE_DIR / gesture).glob("*.png")

    )

    image = ImageLoader.load(

        image_path,

    )

    print(

        "Shape:",

        image.shape,

    )

    print(

        "RGB:",

        ImageLoader.is_rgb(image),

    )

    print(

        "Size:",

        ImageLoader.image_size(image),

    )

    print(

        "Exists:",

        ImageLoader.exists(image_path),

    )


if __name__ == "__main__":

    main()