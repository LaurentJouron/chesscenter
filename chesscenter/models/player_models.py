from tinydb import TinyDB, where, table
from typing import List
import string

from ..utils.constants import DB_PLAYERS
from ..utils.constants import DB_TOURNAMENTS_PLAYERS


class PlayerModel:
    db_players = TinyDB(DB_PLAYERS, indent=4)
    data_players = db_players.table("players")

    db_tournaments_players = TinyDB(DB_TOURNAMENTS_PLAYERS, indent=4)
    data_tp = db_tournaments_players.table("tournaments_players")

    def __init__(self, **kwargs):
        self.id_number: int = kwargs["id_number"]
        self.last_name: str = kwargs["last_name"]
        self.first_name: str = kwargs["first_name"]
        self.birthday: str = kwargs["birthday"]
        self.gender: str = kwargs["gender"]
        self.rank: int = kwargs["rank"]
        self.score = 0.0

    def __repr__(self):
        return (
            f"(Player {self.id_number}: {self.first_name} {self.last_name}, \t"
            f"Gender: {self.gender}, \t"
            f"Birthday: {self.birthday}, \t"
            f"Rank: {self.rank}, \t"
            f"Score: {self.score})\n"
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
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self) -> table.Document:
        return PlayerModel.data_players.get(
            (where("id_number") == self.id_number)
        )

    def save_player(self, validate_data: bool = False) -> int:
        if validate_data:
            self._checks()
        return (
            -1
            if self.exists()
            else PlayerModel.data_players.insert(self.__dict__)
        )

    def _checks(self):
        self._check_names()

    def _check_names(self):
        if not self.first_name:
            raise ValueError("First and last name cannot be blank.")
        special_characters = string.punctuation + string.digits
        for character in self.first_name + self.last_name:
            if character in special_characters:
                raise ValueError(f"Value error {self.full_name}.")

    def exists(self):
        return bool(self.db_instance)

    @classmethod
    def remove_by_code(cls, player_code):
        return cls.data.remove(where("player_code") == player_code)

    @classmethod
    def get_all(cls) -> List["PlayerModel"]:
        return [cls(**player) for player in cls.data_players.all()]

    @classmethod
    def get_one_by_code(cls, player_code) -> "PlayerModel":
        if player_data := cls.data_players.search(
            where("player_code") == player_code
        ):
            return cls(**player_data[0])
        return None

    def update_rank(self, new_rank):
        self.rank = new_rank

    def serialize_player(self):
        return {
            "id_number": self.id_number,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
        }

    def deserialize_player(self):
        """A function to deserialize a player."""

        last_name = self["last_name"]
        first_name = self["first_name"]
        id_number = self["id_number"]
        birth_date = self["birth_date"]
        gender = self["gender"]
        ranking = self["ranking"]
        score = self["score"]
        deserialized_player = PlayerModel(
            last_name=last_name,
            first_name=first_name,
            id_number=id_number,
            birth_date=birth_date,
            gender=gender,
            ranking=ranking,
        )
        deserialized_player.score = score
        return deserialized_player

    def save_tournament_player(self, player_instance):
        PlayerModel.data_tp.insert(player_instance.serialize_player())
