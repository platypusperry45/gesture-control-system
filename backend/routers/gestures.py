from fastapi import APIRouter

from backend.services.gesture_service import gesture_service

router = APIRouter(
    prefix="/gestures",
    tags=["Gestures"],
)


@router.get("/summary")
def summary():

    return gesture_service.dataset_summary()