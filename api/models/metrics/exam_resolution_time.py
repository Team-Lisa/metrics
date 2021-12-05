class ExamResolutionTime:
    NAME = "exam_resolution_time"

    @staticmethod
    def parse(values):
        if len(values) == 0:
            return {
                "time": 0
            }
        return {
            "time": values[0]["value"]
        }