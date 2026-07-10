# Backend API

## Health

GET /health

Returns backend status.

---

## Prediction

POST /predict

Returns:

- gesture
- confidence

---

## Camera

POST /camera/start

Starts webcam.

POST /camera/stop

Stops webcam.

---

## Training

POST /training/start

Starts model training.

POST /training/stop

Stops training.

GET /training/status

Returns live metrics.

---

## Dataset

POST /dataset/capture

Capture gesture images.

GET /dataset/info

Dataset statistics.

---

## Analytics

GET /analytics

Training metrics.

GET /metrics

Model evaluation metrics.