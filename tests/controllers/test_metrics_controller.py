import requests_mock

from api.models.track import Track
from api.repositories.track_repository import TrackRepository
from api.controllers.metrics_controller import MetricsController
from api.services.users import UserService


def test_get_metrics(init):
    from_date = "2021/11/01"
    to_date = "2021/12/20"

    create_track(MetricsController.UNIT_COMPLETED, "2021/11/10", {})
    create_track(MetricsController.UNIT_COMPLETED, "2021/11/10", {})
    create_track(MetricsController.UNIT_COMPLETED, "2021/11/11", {})
    create_track(MetricsController.UNIT_COMPLETED, "2021/11/12", {})

    create_track(MetricsController.NEW_ACCESS, "2021/11/11", {})
    create_track(MetricsController.NEW_ACCESS, "2021/11/11", {})
    create_track(MetricsController.NEW_ACCESS, "2021/11/15", {})
    create_track(MetricsController.NEW_ACCESS, "2021/11/16", {})

    create_track(MetricsController.EXAM_RESOLUTION_TIME, "2021/11/12", {"time": 10.0})
    create_track(MetricsController.EXAM_RESOLUTION_TIME, "2021/11/12", {"time": 20.0})
    create_track(MetricsController.EXAM_RESOLUTION_TIME, "2021/11/13", {"time": 5.5})
    create_track(MetricsController.EXAM_RESOLUTION_TIME, "2021/11/20", {"time": 4.5})

    url = UserService.URL + "users"

    with requests_mock.Mocker() as m:
        json = {
            "users": [
                {
                    "name": "Agustin Horn",
                    "email": "agushorn145@gmail.com",
                    "expo_token": "ExponentPushToken[Sw_KbVJjP1YaqNoaYJIon3]",
                    "last_connection": "2021-11-15",
                    "next_notification": "2021-11-15"
                },
                {
                    "name": "Agustin Horn",
                    "email": "ahorn@fi.uba.ar",
                    "expo_token": "ExponentPushToken[r30NOyEOUW290jLatr72ZD]",
                    "last_connection": "2021-12-05",
                    "next_notification": "2021-11-12"
                },
                {
                    "name": "vik",
                    "email": "vik@gmail.com",
                    "expo_token": "1234",
                    "last_connection": "2021-11-28",
                    "next_notification": "2021-11-29"
                },
                {
                    "name": "Martina Carla Marino",
                    "email": "martinacmarino@gmail.com",
                    "expo_token": "ExponentPushToken[MmZTpBGAsCGhUmESkzOOiE]",
                    "last_connection": "2021-11-29",
                    "next_notification": "2021-11-30"
                },
                {
                    "name": "Gonzalo Marino",
                    "email": "gmarino@fi.uba.ar",
                    "expo_token": "ExponentPushToken[XfAGSYOBmRSvWwCMHx83MJ]",
                    "last_connection": "2021-12-08",
                    "next_notification": "2021-12-08"
                }
            ]
        }
        m.register_uri('GET', url, json=json, status_code=200)

        result = MetricsController.get(from_date, to_date)
        metrics = result["metrics"]

        assert MetricsController.UNIT_COMPLETED in metrics
        assert MetricsController.NEW_ACCESS in metrics
        assert MetricsController.EXAM_RESOLUTION_TIME in metrics
        assert MetricsController.USER_FREQUENCY in metrics

        exam_resolution_time = metrics["exam_resolution_time"]
        access = metrics["new_access"]
        units_completed = metrics["unit_completed"]
        user_frequency = metrics["user_frequency"]

        assert exam_resolution_time["time"] == 10.0
        assert user_frequency["time"] == 21.0

        day_1_access = access[0]
        assert day_1_access["date"] == "2021/11/11"
        assert day_1_access["access_amount"] == 2

        day_2_access = access[1]
        assert day_2_access["date"] == "2021/11/15"
        assert day_2_access["access_amount"] == 1

        day_3_access = access[2]
        assert day_3_access["date"] == "2021/11/16"
        assert day_3_access["access_amount"] == 1

        day_1_units = units_completed[0]
        assert day_1_units["date"] == "2021/11/10"
        assert day_1_units["units_completed_amount"] == 2

        day_2_units = units_completed[1]

        assert day_2_units["date"] == "2021/11/11"
        assert day_2_units["units_completed_amount"] == 1

        day_3_units = units_completed[2]

        assert day_3_units["date"] == "2021/11/12"
        assert day_3_units["units_completed_amount"] == 1

def create_track(name, date, event_data):
    track = Track(
        name=name,
        event_data=event_data,
        date=date
    )
    TrackRepository.add_track(track)
