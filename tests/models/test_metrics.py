from api.models.metrics.units_completed import UnitsCompleted
from api.models.metrics.exam_resolution_time import ExamResolutionTime
from api.models.metrics.user_access import UserAccess


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
