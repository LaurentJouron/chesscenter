import json
from datetime import datetime

from tinydb import TinyDB

from ..utils.constants import DB_PLAYERS
from ..utils.constants import DB_TOURNAMENTS_PLAYERS


class PlayerModel:
    db_players = TinyDB(DB_PLAYERS, indent=4)
    data_players = db_players.table("players")

    db_tournaments_players = TinyDB(DB_TOURNAMENTS_PLAYERS, indent=4)
    data_tp = db_tournaments_players.table("tournaments_players")

    def __init__(self, **kwargs):
        self._id_number: int = kwargs["id_number"]
        self._last_name: str = kwargs["last_name"]
        self._first_name: str = kwargs["first_name"]
        self._birthday: str = kwargs["birthday"]
        self._gender: str = kwargs["gender"]
        self._rank: int = kwargs["rank"]
        self._score: float = kwargs["0"]

    def __repr__(self):
        return (
            f"(Player {self.id_number}: {self.first_name} {self.last_name}, "
            f"Gender: {self.gender}, "
            f"Birthday: {self.birthday}, "
            f"Rank: {self.rank}, "
            f"Score: {self.score})"
        )

    def __str__(self):
        return (
            f"\nPlayer {self.id_number}: "
            f"{self.first_name} {self.last_name}\n"
            f"Gender: {self.gender}\n"
            f"Birthday (YYYY.MM.DD): {self.birthday}\n"
            f"Current rank: {self.rank}\n"
            f"Score: {self.score}"
        )

    @property
    def last_name(self):
        return self._last_name.upper()

    @last_name.setter
    def last_name(self, last_name):
        if not all(char.isalpha() or char.isspace() for char in last_name):
            print("Please enter a valid last name.")
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name.title()

    @first_name.setter
    def first_name(self, first_name):
        if not all(char.isalpha() or char.isspace() for char in first_name):
            print("Please enter a valid first name.")
        self._first_name = first_name

    @property
    def id_number(self):
        return self._id_number

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, new_date):
        try:
            new_date = datetime.strptime(new_date, "%Y.%m.%d").date()
        except ValueError:
            print("Please enter a valid birth date (YYYY.MM.DD).")
        self._birth_date = new_date

    @property
    def gender(self):
        return self._gender.upper()

    @gender.setter
    def gender(self, new_gender):
        if str(new_gender) not in "mMfF" or new_gender.isalpha() is False:
            print("Please enter a valid gender (M/F).")
        self._gender = new_gender

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        if not isinstance(rank, float):
            print("Please enter a valid rank (positive float).")
        self._rank = rank

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score % 0.5 != 0:
            print("Please enter a valid score.")
        self._score = score

    def serialize_player(self):
        serialized_player = {}
        json.dumps(serialized_player, default=str)
        serialized_player["id_number"] = self.id_number
        serialized_player["last_name"] = self.last_name
        serialized_player["first_name"] = self.first_name
        serialized_player["birthday"] = self.birthday
        serialized_player["gender"] = self.gender
        serialized_player["rank"] = self.rank
        serialized_player["score"] = self.score
        return serialized_player

    def deserialize_player(self):
        id_number = self["id_number"]
        last_name = self["last_name"]
        first_name = self["first_name"]
        birthday = self["birthday"]
        gender = self["gender"]
        rank = self["rank"]
        score = self["score"]
        deserialized_player = PlayerModel(
            id_number=id_number,
            last_name=last_name,
            first_name=first_name,
            birthday=birthday,
            gender=gender,
            rank=rank,
        )
        deserialized_player.score = score
        return deserialized_player

    def save_db_tournaments_players(self):
        PlayerModel.data_tp.insert(self)

    def save_db_players(self):
        PlayerModel.data_players.insert(self)
