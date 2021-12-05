from fastapi import APIRouter

from api.controllers.metrics_controller import MetricsController
from api.controllers.tracks_controller import TracksController
from api.models.responses.metrics import Metrics

router = APIRouter(tags=["Metrics"])


@router.get("/metrics", response_model=Metrics)
async def get_metrics(from_date: str = "", to_date: str = ""):
    return MetricsController.get(from_date, to_date)


