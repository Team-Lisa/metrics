from api.controllers.tracks_controller import TracksController
from api.models.requests.track import Track



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
