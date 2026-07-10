# Gesture Control System

An end-to-end AI-powered hand gesture recognition system built using **TensorFlow**, **MediaPipe**, **FastAPI**, **React**, and **Material UI**.

The project enables real-time gesture recognition through a webcam, includes a complete dataset collection and training pipeline, and provides a modern analytics dashboard for monitoring inference and model performance.

---

## Features

### Real-Time Gesture Recognition

- Live webcam streaming
- MediaPipe hand detection
- TensorFlow gesture classification
- Confidence score display
- FPS monitoring
- Stable prediction smoothing
- Automatic camera recovery

---

### Dataset Collection

- Interactive dataset collection tool
- Automatic hand cropping
- Label management
- Image preprocessing
- Dataset organization
- Progress tracking

---

### Model Training

Complete deep learning training pipeline including:

- Dataset splitting
- TensorFlow Dataset API
- Data augmentation
- Early stopping
- Learning rate scheduling
- Checkpoint saving
- Training metrics
- Automatic evaluation
- Model export

---

### Analytics Dashboard

Live dashboard displaying

- Total predictions
- Prediction distribution
- Average confidence
- Average FPS
- CPU usage
- RAM usage
- Camera status
- Model status
- System uptime

---

### Training Dashboard

Interactive training centre featuring

- Live training progress
- Accuracy curve
- Loss curve
- Epoch monitoring
- Console logs
- Dataset overview
- Deployment section
- Training controls

---

### Settings

Application configuration for

- Camera
- AI model
- Backend
- System preferences
- General application settings

---

## Tech Stack

### Frontend

- React
- Vite
- Material UI
- Framer Motion
- Recharts
- Axios

### Backend

- FastAPI
- Uvicorn
- WebSockets

### AI / ML

- TensorFlow
- MediaPipe
- OpenCV
- NumPy
- Scikit-Learn

---

## Project Structure

```
gesture-control-system/

│
├── backend/
│   ├── api/
│   ├── websocket/
│   ├── services/
│   ├── training_manager.py
│   └── training_callback.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── layouts/
│
├── recognition/
│   ├── dataset/
│   ├── network/
│   ├── predictor/
│   ├── training/
│   ├── collector.py
│   └── artifacts/
│
└── README.md
```

---

## Installation

### Clone repository

```bash
git clone https://github.com/<username>/gesture-control-system.git

cd gesture-control-system
```

---

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend runs at

```
http://localhost:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

## Dataset Collection

Launch dataset collector

```bash
python -m recognition.collector
```

Collected images are automatically organized into gesture-specific folders.

---

## Model Training

Train the gesture recognition model

```bash
python -m recognition.training.train
```

Training includes

- augmentation
- checkpointing
- scheduler
- validation
- early stopping
- evaluation
- model export

---

## Running Inference

Start backend

```bash
uvicorn app:app --reload
```

Open frontend

```
http://localhost:5173
```

Allow webcam access to begin live gesture recognition.

---

## Current Gesture Classes

- Open Palm
- Fist
- Peace
- Thumbs Up
- Pointing Up
- OK

*(Can be extended by collecting additional datasets.)*

---

## Model Performance

Current model achieves approximately

- Validation Accuracy: **99%+**
- Test Accuracy: **99%+**
- Real-time inference
- Live confidence estimation

Performance depends on lighting conditions, camera quality, and dataset diversity.

---

## Future Improvements

- Custom gesture creation
- Transfer learning support
- ONNX export
- TensorRT acceleration
- Mobile deployment
- Multi-hand recognition
- Gesture sequences
- Voice feedback
- Cloud deployment
- User authentication
- Training history database


---

## License

This project is intended for educational and portfolio purposes.

---

## Author

**Akshat Yadav**

Artificial Intelligence | Machine Learning | Computer Vision | Full Stack AI Applications

GitHub:
https://github.com/platypusperry45

LinkedIn:
https://www.linkedin.com/in/akshat-yadav-b22246377?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app