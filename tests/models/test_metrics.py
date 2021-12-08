import requests_mock

from api.models.metrics.units_completed import UnitsCompleted
from api.models.metrics.exam_resolution_time import ExamResolutionTime
from api.models.metrics.user_access import UserAccess
from api.models.metrics.user_frequency import UserFrequency
from api.services.users import UserService


def test_user_access_parse_with_empty_data():
    assert len(UserAccess.parse([])) == 0


def test_units_completed_parse_with_empty_data():
    assert len(UnitsCompleted.parse([])) == 0


def test_exam_resolution_time_parse_with_empty_data():
    assert ExamResolutionTime.parse([]) == {
        "time": 0
    }


def test_user_access_parse():
    data = [
        {
            "value": 3,
            "_id": {
                "date": "2021/11/11",
                "name": "new_access"
            }
        }
    ]

    assert UserAccess.parse(data) == [
        {
            "access_amount": 3,
            "date": "2021/11/11"
        }
    ]


def test_units_completed_parse():
    data = [
        {
            "value": 3,
            "_id": {
                "date": "2021/11/11",
                "name": "unit_completed"
            }
        }
    ]

    assert UnitsCompleted.parse(data) == [
        {
            "units_completed_amount": 3,
            "date": "2021/11/11"
        }
    ]


def test_exam_resolution_time_parse():
    data = [
        {
            "value": 3.0,
            "_id": {
                "name": "exam_resolution_time"
            }
        }
    ]
    assert ExamResolutionTime.parse(data) == {
        "time": 3.0
    }


def test_user_frequency():
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

        result = UserFrequency.get("2021/12/01", "2021/12/20")

        assert result == 13.5
        # esto es 2021-12-08 hasta el 20 hay 12 dias
        # y 2021-12-05 al 20 son 15 en total 27
        # en la ventana del tiempo seleccionada solo hay 2 usuarios
        # por lo tanto el resultado es 13.5
