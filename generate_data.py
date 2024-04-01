from datetime import datetime, timedelta
from faker import Faker
import random

from chesscenter.utils.constants import BIRTHDAY_LIMIT
from chesscenter.utils.constants import START_MIN
from chesscenter.utils.constants import COUNT_RANDOM_PLAYER
from chesscenter.utils.constants import COUNT_RANDOM_TOURNAMENT
from chesscenter.models.player_models import PlayerModel
from chesscenter.models.tournament_models import TournamentModel

from chesscenter.controllers.player_controllers import PlayerRandomController


fake = Faker()


class PlayerGenerateData:
    gender = ["M", "F"]

    def __init__(self):
        self.model = PlayerModel

    def generate_player(self):
        print("New players are being created...\n")
        for _ in range(COUNT_RANDOM_PLAYER):
            id_number = random.randint(100000, 999999)
            last_name = fake.first_name()
            gender = random.choice(self.gender)
            first_name = self.generate_firstname(gender)
            rank = random.randint(1, 500)
            birthday = self.generate_date()
            player_instance = self.model(
                id_number=id_number,
                last_name=last_name,
                first_name=first_name,
                birthday=birthday,
                gender=gender,
                rank=rank,
            )
            player_instance.save_player()
        print("New players have been created...\n")

    def generate_date(self):
        random_year = random.randint(1900, BIRTHDAY_LIMIT.year)
        random_month = random.randint(1, 12)
        random_day = random.randint(1, 28)
        random_date = datetime(random_year, random_month, random_day)
        return random_date.strftime("%Y.%m.%d")

    def generate_firstname(self, gender):
        if gender == "M":
            return fake.first_name_male()
        elif gender == "F":
            return fake.first_name_female()


class TournamentGenerateData:
    time_control = ["Blitz", "Rapid", "Bullet"]

    def __init__(self):
        self.model = TournamentModel
        self.today = START_MIN

    def generate_tournament(self):
        print("New tournaments are being created...\n")
        for _ in range(COUNT_RANDOM_TOURNAMENT):
            name = fake.word()
            location = fake.country()
            start_date = self.generate_start_date()
            end_date = self.generate_end_date(start_date=start_date)
            description = self._get_string("Enter a comment if needed: ")
            time_controle = random.choice(self.time_control)
            players_list = PlayerRandomController()
            tournament_instance = self.model(
                name=name,
                location=location,
                start_date=start_date,
                end_date=end_date,
                description=description,
                time_controle=time_controle,
                players_list=players_list,
            )
            tournament_instance.save_tournament()
        print("New players have been created...\n")

    def generate_start_date(self, default=True):
        if default:
            return self.today.strftime("%Y.%m.%d")
        while True:
            year = random.randint(self.today.year, self.today.year + 1)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            start_date = datetime(year, month, day).date()
            if start_date >= self.today:
                return start_date.strftime("%Y.%m.%d")

    def generate_end_date(self, start_date):
        start_date = datetime.strptime(start_date, "%Y.%m.%d").date()
        end_date = start_date + timedelta(days=1)
        return end_date.strftime("%Y.%m.%d")


player = PlayerGenerateData()
player.generate_player()

tournament = TournamentGenerateData()
tournament.generate_tournament()
