from api.models.track import Track


def test_model_to_json():
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
    assert track.to_json() == {
        "name": name,
        "event_data": event_data,
        "date": date
    }
