class UnitsCompleted:

    @staticmethod
    def parse(values):
        if len(values) == 0:
            return []

        return list(
            map(
                lambda value: {"date": value["_id"]["date"], "units_completed_amount": value["value"]},
                values
            )
        )