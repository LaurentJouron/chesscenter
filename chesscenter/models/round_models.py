import json
from datetime import datetime


class RoundModel:
    number_of_rounds = 0
    list_of_matches = []

    def __init__(self, **kwargs):
        RoundModel.number_of_rounds += 1
        self._matches: str = kwargs["matches"]
        self._round_name: str = f"Round {RoundModel.number_of_rounds}"
        self._start_date: str = kwargs["start_date"]
        self._end_date: str = kwargs["end_date"]

    def __repr__(self):
        return (
            f"({self.round_name} \n"
            f"- From {self.start_date} to {self.end_date}\n"
            f"- Matches: {self.matches})"
        )

    def __str__(self):
        return (
            f"\n{self.round_name}: from {self.start_date} to {self.end_date}\n"
            f"Matches: {self.matches[0]}, {self.matches[1]}, "
            f"{self.matches[2]}, {self.matches[3]}"
        )

    @property
    def matches(self):
        return self._matches

    @matches.setter
    def matches(self, new_matches):
        if not (isinstance(new_matches, list) and len(new_matches) == 4):
            print("Please enter a valid list of matches.")
        self._matches = new_matches

    @property
    def round_name(self):
        return self._round_name.capitalize()

    @round_name.setter
    def round_name(self, new_name):
        if not isinstance(new_name, int):
            print("Please enter a valid round name.")
        self._round_name = new_name

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_date):
        try:
            new_date = datetime.strptime(new_date, "%Y.%m.%d (%H:%M:%S)")
        except ValueError:
            print("Please enter a valid date (YYYY.MM.DD (HH:MM:SS))")
        self._start_date = new_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_date):
        try:
            new_date = datetime.strptime(new_date, "%Y.%m.%d (%H:%M:%S)")
        except ValueError:
            print("Please enter a valid date (YYYY.MM.DD (HH:MM:SS))")
        self._end_date = new_date

    def serialize_round(self):
        serialized_round = {}
        json.dumps(serialized_round, default=str)
        serialized_round["matches"] = self.matches
        serialized_round["start_date"] = self.start_date.strftime(
            "%Y.%m.%d (%H:%M:%S)"
        )
        serialized_round["end_date"] = self.end_date.strftime(
            "%Y.%m.%d (%H:%M:%S)"
        )
        return serialized_round

    def deserialize_round(self):
        """A function to deserialize a round."""

        matches = self["matches"]
        start_date = self["start_date"]
        end_date = self["end_date"]
        return RoundModel(
            matches=matches, start_date=start_date, end_date=end_date
        )
