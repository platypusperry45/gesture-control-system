from recognition.config import GESTURES

from recognition.predictor import (
    ModelLoader,
)


def main():

    loader = ModelLoader(

        num_classes=len(GESTURES),

    )

    print(loader)


if __name__ == "__main__":

    main()