import asyncio

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.manager import manager
from backend.main import inference_service

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:

        while True:

            prediction = inference_service.latest_prediction

            await websocket.send_json(
                prediction or {}
            )

            await asyncio.sleep(0.05)

    except WebSocketDisconnect:

        manager.disconnect(websocket)