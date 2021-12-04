import pytest

from api.controllers.tracks_controller import TracksController
from api.models.requests.track import Track
from fastapi import HTTPException


def test_response(init):
    name = "mockname"
    event_data = {
        "time": 3.134
    }
    date = "2021/11/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    response = TracksController.create(track)
    assert response == {
        "message": "track saved"
    }


def test_user_not_found(init):
    name = "mockname"

    with pytest.raises(HTTPException) as e_info:
        TracksController.find_by_name(name)
