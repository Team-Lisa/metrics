from api.repositories.track_repository import TrackRepository
from api.models.track import Track


def test_add_track_successfully(init):
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
    result = TrackRepository.add_track(track)
    assert result.name == name
    assert result.event_data == event_data
    assert result.date == date

def test_get_track_by_name_successfully(init):
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
    TrackRepository.add_track(track)
    result = TrackRepository.get_track_by_name(name)
    assert result[0].name == name


def test_delete_all_users(init):
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
    TrackRepository.add_track(track)
    TrackRepository.delete_all_track()
    result = TrackRepository.get_all_tracks()
    assert result.count() == 0
