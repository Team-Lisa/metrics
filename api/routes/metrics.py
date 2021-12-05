from fastapi import APIRouter
from api.controllers.tracks_controller import TracksController


router = APIRouter(tags=["Metrics"])

@router.get("/metrics")
async def find_user(name: str = ""):
    return TracksController.find_by_name(name)


