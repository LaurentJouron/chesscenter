from datetime import datetime
from faker import Faker
import random

from ..utils.constants import BIRTHDAY_LIMIT, COUNT_RANDOM_PLAYER
from ..models.player_models import PlayerModel

fake = Faker()


class RandomPlayer:
    gender = ["M", "F"]

    def generate_players():
        id_number = random.randint(100000, 999999)
        last_name = fake.first_name()
        gender = random.choice(RandomPlayer.gender)
        first_name = RandomPlayer.generate_firstname(gender)
        rank = random.randint(1, 500)
        birthday = RandomPlayer.generate_date()
        return PlayerModel(
            id_number=id_number,
            last_name=last_name,
            first_name=first_name,
            birthday=birthday,
            gender=gender,
            rank=rank,
        )

    def generate_date():
        random_year = random.randint(1900, BIRTHDAY_LIMIT.year)
        random_month = random.randint(1, 12)
        random_day = random.randint(1, 28)
        random_date = datetime(random_year, random_month, random_day)
        return random_date.strftime("%Y.%m.%d")

    def generate_firstname(self):
        if self == "M":
            return fake.first_name_male()
        elif self == "F":
            return fake.first_name_female()


if __name__ == "__main__":

    for _ in range(COUNT_RANDOM_PLAYER):
        player = RandomPlayer.generate_players()
        serialized_player = PlayerModel.serialize_player(player)
        PlayerModel.save_player_to_database(serialized_player)
