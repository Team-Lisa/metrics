from fastapi import APIRouter
from api.models.requests.track import Track
from api.controllers.tracks_controller import TracksController
from api.models.responses.track import Track as TrackResponse

router = APIRouter(tags=["Tracks"])


@router.post("/tracks", response_model=TrackResponse)
async def create_user(track: Track):
    return TracksController.create(track)


@router.get("/metrics")
async def find_user(name: str = ""):
    return TracksController.find_by_name(name)


