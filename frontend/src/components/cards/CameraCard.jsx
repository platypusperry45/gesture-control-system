export default function CameraCard() {

    console.log("CameraCard is rendering");

    return (
        <div
            style={{
                background: "red",
                padding: 20,
                color: "white",
                fontSize: 24,
            }}
        >
            CAMERA CARD IS HERE

            <br /><br />

            <img
                src="http://127.0.0.1:8000/video_feed"
                alt="camera"
                width="600"
            />
        </div>
    );
}