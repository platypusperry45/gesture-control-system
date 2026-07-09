export function connectTrainingSocket(onMessage) {

    const socket = new WebSocket(
        "ws://127.0.0.1:8000/ws/training"
    );

    socket.onmessage = (event) => {

        const data = JSON.parse(event.data);

        onMessage(data);

    };

    socket.onclose = () => {

        console.log("Training socket disconnected");

    };

    return socket;

}