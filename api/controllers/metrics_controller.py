from api.models.metrics.exam_resolution_time import ExamResolutionTime
from api.models.metrics.units_completed import UnitsCompleted
from api.models.metrics.user_access import UserAccess
from api.repositories.track_repository import TrackRepository


class MetricsController:
    EXAM_RESOLUTION_TIME = "exam_resolution_time"
    UNIT_COMPLETED = "unit_completed"
    NEW_ACCESS = "new_access"
    USER_FREQUENCY = "user_frequency"

    @staticmethod
    def get(from_date, to_date):
        result = {}

        MetricsController.add_exam_resolution_time(result, from_date, to_date)
        MetricsController.add_access_per_day(result, from_date, to_date)
        MetricsController.add_units_completed_per_day(result, from_date, to_date)

        return {"metrics": result}

    @staticmethod
    def get_match(name, from_date, to_date):
        return {
            "$and": [{"$expr": {"$gte": ["$date", from_date]}},
                     {"$expr": {"$lte": ["$date", to_date]}}
                     ],
            "name": name

        }

    @staticmethod
    def add_exam_resolution_time(result, from_date, to_date):
        exam_resolution_time = list(TrackRepository.get_statistics(
            match=MetricsController.get_match(MetricsController.EXAM_RESOLUTION_TIME, from_date, to_date),
            group={
                "_id": {
                    "name": "$name"
                },
                "value": {"$avg": "$event_data.time"}
            }
        ))

        result[MetricsController.EXAM_RESOLUTION_TIME] = ExamResolutionTime.parse(exam_resolution_time)


    @staticmethod
    def add_access_per_day(result, from_date, to_date):
        access_per_day = list(TrackRepository.get_statistics(
            match=MetricsController.get_match(MetricsController.NEW_ACCESS, from_date, to_date),
            group={
                "_id": {
                    "name": "$name",
                    "date": "$date"
                },
                "value": {"$sum": 1}
            }
        ))

        result[MetricsController.NEW_ACCESS] = UserAccess.parse(access_per_day)

    @staticmethod
    def add_units_completed_per_day(result, from_date, to_date):
        units_completed_per_day = list(TrackRepository.get_statistics(
            match=MetricsController.get_match(MetricsController.UNIT_COMPLETED, from_date, to_date),
            group={
                "_id": {
                    "name": "$name",
                    "date": "$date"
                },
                "value": {"$sum": 1}
            }
        ))

        result[MetricsController.UNIT_COMPLETED] = UnitsCompleted.parse(units_completed_per_day)
