from datetime import datetime
from faker import Faker
import random

from ..utils.constants import COUNT_RANDOM_PLAYER
from ..utils.constants import BIRTHDAY_LIMIT
from ..utils.bases.controllers import BaseController
from ..models.player_models import PlayerModel
from ..views.player_views import PlayerView
from ..controllers import home_controllers as home

fake = Faker()
view = PlayerView()


class PlayerController(BaseController):
    def __init__(self):
        self.model = PlayerModel

    def run(self):
        view.display_reception()
        while True:
            choice = view.display_menu(view.player_menu)
            if choice == "1":
                return PlayerGenerateController()
            elif choice == "2":
                return PlayerGetAllController()
            elif choice == "3":
                return PlayerCreateController()
            elif choice == "4":
                return PlayerGetDetailController()

            elif choice == "5":
                return home.HomeController()


class PlayerGenerateController(PlayerController):
    gender = ["M", "F"]

    def __init__(self):
        self.model = PlayerModel

    def run(self):
        print("generate")
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
        return PlayerController()

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


class PlayerGetAllController(PlayerController):
    def __init__(self) -> None:
        self.model = PlayerModel

    def run(self):
        # view.display_list()
        print(self.model.get_all())
        return PlayerController()


class PlayerCreateController(PlayerController):
    def __init__(self):
        self.model = PlayerModel

    def run(self):
        print("create")
        return PlayerController()


class PlayerGetDetailController(PlayerController):
    def __init__(self):
        self.model = PlayerModel

    def run(self):
        print("datails")
        return PlayerController()
