"""
FastAPI Backend
"""

from __future__ import annotations

import json
import threading
import time
import traceback
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
import asyncio
from backend.streaming.camera_stream import CameraStreamer
from backend.training_manager import TrainingManager
from recognition.training.train import main as train_model
from recognition.predictor import ModelLoader
from recognition.predictor.inference import InferenceEngine
from backend.routers.actions import router as actions_router
from backend.routers.dataset import router as dataset_router
from backend.routers.gestures import router as gestures_router

app = FastAPI(
    title="Gesture Control Backend",
    version="1.0.0",
)


app.include_router(actions_router)
app.include_router(dataset_router)
app.include_router(gestures_router)

# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():

    print("=" * 60)
    print("Backend Starting...")
    print("=" * 60)

    try:

        model_loader.load()

        print("Gesture model loaded.")

    except Exception as e:

        print("Could not load gesture model.")
        print(e)

# ==========================================================
# Runtime State
# ==========================================================

START_TIME = time.time()

system_state = {
    "camera": False,
    "model_loaded": True,
    "inference_running": False,
    "prediction": None,
    "confidence": 0.0,
    "action": None,
    "fps": 0.0,
    "hand_detected": False,
}

# ==========================================================
# Inference Engine
# ==========================================================

CLASS_NAMES = [

    "open_palm",

    "fist",

    "peace",

    "thumbs_up",

    "point",

    "okay",

]

engine = InferenceEngine(

    checkpoint_path="recognition/artifacts/checkpoints/best.weights.h5",

    class_names=CLASS_NAMES,

)

camera_stream = CameraStreamer(
    engine,
    system_state,
)

model_loader = ModelLoader(
    num_classes=6,
    checkpoint_path="recognition/artifacts/trained_models/gesture_recognition.weights.h5",
)

training = TrainingManager()

# ==========================================================
# Paths
# ==========================================================

DATASET_DIR = (
    Path(__file__).resolve().parent.parent
    / "recognition"
    / "data"
    / "raw"
    / "images"
)

MAPPINGS_FILE = (
    Path(__file__).resolve().parent
    / "data"
    / "action_mappings.json"
)

MAPPINGS_FILE.parent.mkdir(exist_ok=True)

if not MAPPINGS_FILE.exists():
    MAPPINGS_FILE.write_text("{}")


# ==========================================================
# Request Models
# ==========================================================

class GestureRequest(BaseModel):
    name: str


class RenameGestureRequest(BaseModel):
    new_name: str


class ActionMapping(BaseModel):
    gesture: str
    type: str
    action: str
    enabled: bool = True


# ==========================================================
# Helpers
# ==========================================================

def get_uptime():

    elapsed = int(time.time() - START_TIME)

    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


def load_mappings():

    with open(MAPPINGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_mappings(data):

    with open(MAPPINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
        )


# ==========================================================
# Training Thread
# ==========================================================

def run_training():

    training.reset()

    training.running = True
    training.completed = False
    training.error = None

    try:

        train_model(training)

        training.completed = True
        training.add_log("Training finished successfully.")

    except Exception as e:

        traceback.print_exc()

        training.completed = False
        training.error = str(e)

        training.add_log(f"ERROR: {e}")

    finally:

        training.running = False

# ==========================================================
# Root
# ==========================================================

@app.get("/")
def root():

    return {
        "message": "Gesture Control Backend Running"
    }


# ==========================================================
# Health
# ==========================================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# ==========================================================
# Status
# ==========================================================

@app.get("/status")
def status():

    return {

        "uptime": round(
            time.time() - START_TIME,
            1,
        ),

        **system_state,

    }

@app.websocket("/ws/status")
async def websocket_status(websocket: WebSocket):

    await websocket.accept()

    try:

        while True:

            await websocket.send_json(

                {

                    "uptime": round(
                        time.time() - START_TIME,
                        1,
                    ),

                    **system_state,

                }

            )

            await asyncio.sleep(0.05)

    except WebSocketDisconnect:

        print("Dashboard disconnected.")

# ==========================================================
# Live Camera Stream
# ==========================================================

@app.get("/video_feed")
def video_feed():

    return StreamingResponse(
        camera_stream.generate(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )


# ==========================================================
# Controls
# ==========================================================

@app.post("/start")
def start():

    system_state["camera"] = True
    system_state["inference_running"] = True

    return {

        "success": True,

        "message": "Inference Started",

    }


@app.post("/stop")
def stop():

    system_state["camera"] = False
    system_state["inference_running"] = False
    system_state["prediction"] = None
    system_state["confidence"] = 0.0
    system_state["action"] = None
    system_state["fps"] = 0.0

    return {

        "success": True,

        "message": "Inference Stopped",

    }


@app.post("/mock")
def mock_prediction():

    system_state["camera"] = True
    system_state["inference_running"] = True
    system_state["prediction"] = "thumbs_up"
    system_state["confidence"] = 0.98
    system_state["action"] = "Volume Up"
    system_state["fps"] = 29.8

    return {

        "success": True,

        "message": "Mock Prediction Updated",

    }

# ==========================================================
# Gesture Dataset Management
# ==========================================================

@app.get("/gestures")
def get_gestures():

    DATASET_DIR.mkdir(parents=True, exist_ok=True)

    gestures = sorted(
        [
            folder.name
            for folder in DATASET_DIR.iterdir()
            if folder.is_dir()
        ]
    )

    return {
        "gestures": gestures
    }


@app.post("/gestures")
def create_gesture(request: GestureRequest):

    name = request.name.strip()

    if not name:

        raise HTTPException(
            status_code=400,
            detail="Gesture name cannot be empty.",
        )

    folder = DATASET_DIR / name

    if folder.exists():

        raise HTTPException(
            status_code=400,
            detail="Gesture already exists.",
        )

    folder.mkdir(parents=True)

    return {

        "success": True,

        "gesture": name,

    }


@app.put("/gestures/{gesture}")
def rename_gesture(
    gesture: str,
    request: RenameGestureRequest,
):

    old_folder = DATASET_DIR / gesture
    new_folder = DATASET_DIR / request.new_name.strip()

    if not old_folder.exists():

        raise HTTPException(
            status_code=404,
            detail="Gesture not found.",
        )

    if new_folder.exists():

        raise HTTPException(
            status_code=400,
            detail="Target gesture already exists.",
        )

    old_folder.rename(new_folder)

    return {

        "success": True,

        "gesture": request.new_name,

    }


@app.delete("/gestures/{gesture}")
def delete_gesture(gesture: str):

    import shutil

    folder = DATASET_DIR / gesture

    if not folder.exists():

        raise HTTPException(
            status_code=404,
            detail="Gesture not found.",
        )

    shutil.rmtree(folder)

    return {

        "success": True

    }
# ==========================================================
# Action Mappings
# ==========================================================

@app.get("/mappings")
def get_mappings():

    return load_mappings()


@app.post("/mappings")
def save_mapping(mapping: ActionMapping):

    mappings = load_mappings()

    mappings[mapping.gesture] = {
        "type": mapping.type,
        "action": mapping.action,
        "enabled": mapping.enabled,
    }

    save_mappings(mappings)

    return {
        "success": True,
    }


@app.put("/mappings/{gesture}")
def update_mapping(
    gesture: str,
    mapping: ActionMapping,
):

    mappings = load_mappings()

    if gesture not in mappings:

        raise HTTPException(
            status_code=404,
            detail="Mapping not found.",
        )

    mappings[gesture] = {
        "type": mapping.type,
        "action": mapping.action,
        "enabled": mapping.enabled,
    }

    save_mappings(mappings)

    return {
        "success": True,
    }


@app.delete("/mappings/{gesture}")
def delete_mapping(gesture: str):

    mappings = load_mappings()

    if gesture in mappings:

        del mappings[gesture]

        save_mappings(mappings)

    return {
        "success": True,
    }


@app.post("/mappings/toggle/{gesture}")
def toggle_mapping(gesture: str):

    mappings = load_mappings()

    if gesture not in mappings:

        raise HTTPException(
            status_code=404,
            detail="Mapping not found.",
        )

    mappings[gesture]["enabled"] = not mappings[gesture].get(
        "enabled",
        True,
    )

    save_mappings(mappings)

    return {
        "success": True,
        "enabled": mappings[gesture]["enabled"],
    }

# ==========================================================
# Training
# ==========================================================

@app.post("/training/start")
def start_training():

    if training.running:

        return {
            "success": False,
            "message": "Training already running.",
        }

    thread = threading.Thread(
        target=run_training,
        daemon=True,
    )

    thread.start()

    return {
        "success": True,
        "message": "Training started.",
    }


@app.get("/training/status")
def training_status():

    return {

        "running": training.running,

        "completed": training.completed,

        "error": training.error,

        "epoch": training.epoch,

        "total_epochs": training.total_epochs,

        "loss": training.loss,

        "val_loss": training.val_loss,

        "accuracy": training.accuracy,

        "val_accuracy": training.val_accuracy,

        "progress": training.progress,

    }

@app.get("/model/status")
def model_status():

    return {

        "loaded": model_loader.loaded,

        "checkpoint": str(model_loader.checkpoint_path),

    }

@app.get("/training/logs")
def training_logs():

    return training.logs


@app.post("/training/reset")
def reset_training():

    if training.running:

        raise HTTPException(
            status_code=400,
            detail="Training is currently running.",
        )

    training.reset()

    return {
        "success": True,
    }


@app.get("/dataset/stats")
def dataset_stats():

    dataset_dir = DATASET_DIR

    dataset_dir.mkdir(parents=True, exist_ok=True)

    classes = [
        folder
        for folder in dataset_dir.iterdir()
        if folder.is_dir()
    ]

    image_extensions = {
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".webp",
    }

    total_images = sum(
        len(
            [
                file
                for file in folder.iterdir()
                if file.suffix.lower() in image_extensions
            ]
        )
        for folder in classes
    )

    return {

        "images": total_images,

        "classes": len(classes),

        "epochs": training.total_epochs,

        "accuracy": round(training.val_accuracy * 100, 2),

    }

@app.get("/training/history")
def training_history():

    return training.history

@app.websocket("/ws/training")
async def websocket_training(websocket: WebSocket):

    await websocket.accept()

    try:

        while True:

            await websocket.send_json(
                {
                    "running": training.running,
                    "completed": training.completed,
                    "epoch": training.epoch,
                    "total_epochs": training.total_epochs,
                    "loss": training.loss,
                    "accuracy": training.accuracy,
                    "progress": training.progress,
                    "logs": training.logs[-30:],
                }
            )

            await asyncio.sleep(0.3)

    except WebSocketDisconnect:

        print("Training dashboard disconnected.")
        
# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )