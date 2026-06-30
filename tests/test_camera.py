from recognition.predictor import Camera


def main():

    camera = Camera()

    while True:

        frame = camera.read()

        if frame is None:

            break

        camera.show(

            "Camera",

            frame,

        )

        if camera.should_close():

            break

    camera.close()


if __name__ == "__main__":

    main()