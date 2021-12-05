from mongomock import ObjectId

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


def test_filter_by_name_statistics(init):
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

    name = "mockname2"
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

    result = list(TrackRepository.get_statistics(match={"name": "mockname2"}))
    assert len(result) == 1

def test_filter_by_date_statistics(init):
    from_date = "2021/11/01"
    to_date = "2021/12/15"

    name = "mockname"
    event_data = {
        "time": 3.134
    }
    date = "2021/12/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname2"
    event_data = {
        "time": 3.134
    }
    date = "2021/07/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname3"
    event_data = {
        "time": 3.134
    }
    date = "2021/12/20"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    result = list(TrackRepository.get_statistics(match={
        "$and": [{"$expr": {"$gte": ["$date", from_date]}},
                 {"$expr": {"$lte": ["$date", to_date]}}
                 ]}
    ))

    assert len(result) == 1
    track = result[0]
    assert track["name"] == "mockname"
    assert track["date"] == "2021/12/10"


def test_filter_by_date_and_name_statistics(init):
    from_date = "2021/11/01"
    to_date = "2021/12/15"

    name = "mockname"
    event_data = {
        "time": 3.134
    }
    date = "2021/12/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname2"
    event_data = {
        "time": 3.134
    }
    date = "2021/07/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname3"
    event_data = {
        "time": 3.134
    }
    date = "2021/12/20"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    result = list(TrackRepository.get_statistics(match={
        "$and": [{"$expr": {"$gte": ["$date", from_date]}},
                 {"$expr": {"$lte": ["$date", to_date]}}
                 ],
        "name": "mockname"

    }
    ))

    assert len(result) == 1
    track = result[0]
    assert track["name"] == "mockname"
    assert track["date"] == "2021/12/10"

def test_filter_by_date_and_name_and_group_statistics(init):
    from_date = "2021/11/01"
    to_date = "2021/12/15"

    name = "mockname"
    event_data = {
        "time": 10.0
    }
    date = "2021/12/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname"
    event_data = {
        "time": 5.0
    }
    date = "2021/12/11"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname2"
    event_data = {
        "time": 3.134
    }
    date = "2021/07/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname3"
    event_data = {
        "time": 3.134
    }
    date = "2021/12/20"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    result = list(TrackRepository.get_statistics(match={
        "$and": [{"$expr": {"$gte": ["$date", from_date]}},
                 {"$expr": {"$lte": ["$date", to_date]}}
                 ],
        "name": "mockname"

    },
        group={
            "_id": {
                "name": "$name",
                "date": "$date",
            },
            "value": {"$avg": "$event_data.time"}
        }
    ))

    assert len(result) == 2


def test_filter_by_date_and_name_and_group_mean_statistics(init):
    from_date = "2021/11/01"
    to_date = "2021/12/15"

    name = "mockname"
    event_data = {
        "time": 10.0
    }
    date = "2021/12/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname"
    event_data = {
        "time": 5.0
    }
    date = "2021/12/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname2"
    event_data = {
        "time": 3.134
    }
    date = "2021/07/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname3"
    event_data = {
        "time": 3.134
    }
    date = "2021/12/20"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    result = list(TrackRepository.get_statistics(match={
        "$and": [{"$expr": {"$gte": ["$date", from_date]}},
                 {"$expr": {"$lte": ["$date", to_date]}}
                 ],
        "name": "mockname"

    },
        group={
            "_id": {
                "name": "$name",
                "date": "$date",
            },
            "value": {"$avg": "$event_data.time"}
        }
    ))

    assert len(result) == 1
    assert result[0]["value"] == 7.5

def test_filter_by_date_and_name_and_group_count_statistics(init):
    from_date = "2021/11/01"
    to_date = "2021/12/21"

    name = "mockname"
    event_data = {
        "time": 10.0
    }
    date = "2021/12/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname"
    event_data = {
        "time": 5.0
    }
    date = "2021/12/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname2"
    event_data = {
        "time": 3.134
    }
    date = "2021/07/10"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    name = "mockname"
    event_data = {
        "time": 3.134
    }
    date = "2021/12/20"
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)

    result = list(TrackRepository.get_statistics(match={
        "$and": [{"$expr": {"$gte": ["$date", from_date]}},
                 {"$expr": {"$lte": ["$date", to_date]}}
                 ],
        "name": "mockname"

    },
        group={
            "_id": {
                "name": "$name",
                "date": "$date",
            },
            "value": {"$sum": 1}
        }
    ))

    assert len(result) == 2
