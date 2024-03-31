import json
import random
from datetime import datetime, timedelta
from ..utils.constants import NUMBER_OF_DAY


class RandomRound:
    dates_attributed = []

    @staticmethod
    def generate_random_round():
        """Generate random start and end dates for a round."""
        start_date, end_date = RandomRound.generate_dates()
        return (start_date, end_date)

    @staticmethod
    def generate_dates():
        """Generate random start and end dates."""
        current_date = datetime.now()

        start_year = random.randint(2024, 2025)
        start_month = random.randint(1, 12)
        start_day = random.randint(1, 28)
        start_hour = random.choice([8, 11, 15, 17])
        start_minutes = random.choice([0, 30])
        start_date = datetime(
            start_year, start_month, start_day, start_hour, start_minutes
        )

        min_duration = timedelta(days=NUMBER_OF_DAY)
        end_date = start_date + min_duration

        while end_date < current_date:
            end_year = random.randint(start_year, 2025)
            end_month = random.randint(start_month, 12)
            end_day = random.randint(start_day, 28)
            end_hour = random.choice([8, 11, 15, 17])
            end_minutes = random.choice([0, 30])
            end_date = datetime(
                end_year, end_month, end_day, end_hour, end_minutes
            )

        return start_date, end_date

    def serialize_random_round(self, start_date, end_date):
        """Serialize round data into a JSON object."""
        serialized_round = {
            "matches": self.matches,
            "start_date": start_date.strftime("%Y.%m.%d (%H:%M:%S)"),
            "end_date": end_date.strftime("%Y.%m.%d (%H:%M:%S)"),
        }
        return json.dumps(serialized_round, default=str)
