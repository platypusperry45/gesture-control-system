"""
FastAPI Backend
"""

from __future__ import annotations

import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from streaming.camera_stream import CameraStreamer

app = FastAPI(
    title="Gesture Control Backend",
    version="1.0.0",
)

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
}

camera_stream = CameraStreamer()

# ==========================================================
# Helpers
# ==========================================================

def get_uptime() -> str:

    elapsed = int(time.time() - START_TIME)

    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


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

        **system_state,

        "uptime": get_uptime(),

    }


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
# Run
# ==========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )