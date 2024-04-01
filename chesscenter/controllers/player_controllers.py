from datetime import datetime
from faker import Faker
import random

from ..utils.constants import BIRTHDAY_LIMIT, NUMBER_OF_PLAYERS
from ..utils.bases.controllers import BaseController
from ..models.player_models import PlayerModel
from ..views.player_views import PlayerView
from . import home_controllers as home
from generate_data import PlayerGenerateData

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
                view.display_details()
                while True:
                    search = view.display_menu(view.search_player)
                    if search == "1":
                        return PlayerGetByRankController()
                    if search == "2":
                        return PlayerGetByLastnameController()
                    if search == "3":
                        return PlayerGetByIdController()

            elif choice == "5":
                return home.HomeController()


class PlayerGenerateController(PlayerController, PlayerGenerateData):
    gender = ["M", "F"]

    def __init__(self):
        self.model = PlayerModel

    def run(self):
        self.generate_player()
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
        view.display_generate()
        print(self.model.get_all())
        return PlayerController()


class PlayerCreateController(PlayerController):
    def __init__(self):
        self.model = PlayerModel

    def run(self):
        view.display_creation()
        view.enter_information()
        player_data = view.get_data()
        player = self.model(
            id_number=player_data["id_number"],
            last_name=player_data["last_name"],
            first_name=player_data["first_name"],
            birthday=player_data["birthday"].strftime("%Y.%m.%d"),
            gender=player_data["gender"],
            rank=player_data["rank"],
        )
        player.save_player()
        view.player_register(
            f"{player_data['first_name']} {player_data['last_name']}"
        )
        return PlayerController()


class PlayerGetByRankController(PlayerController):
    def __init__(self):
        self.model = PlayerModel

    def run(self):
        rank = view.get_player_rank()
        while True:
            if player := self.model.get_player_by_rank(rank=rank):
                view.display_player(player=player)
            else:
                view._message_error(var=rank)

            return PlayerController()


class PlayerGetByLastnameController(PlayerController):
    def __init__(self):
        self.model = PlayerModel

    def run(self):
        lastname = view.get_player_lastname()
        while True:
            if player := self.model.get_player_by_lastname(last_name=lastname):
                view.display_player(player=player)
            else:
                view._message_error(var=lastname)

            return PlayerController()


class PlayerGetByIdController(PlayerController):
    def __init__(self):
        self.model = PlayerModel

    def run(self):
        id_number = view.get_player_id()
        while True:
            if player := self.model.get_player_by_id(id_number=id_number):
                view.display_player(player=player)
            else:
                view._message_error(var=id_number)

            return PlayerController()


class PlayerLoadRandomController(PlayerController):
    def __init__(self):
        self.model = PlayerModel

    def run(self, num_players=NUMBER_OF_PLAYERS):
        """
        Load a random selection of players from the given list of players.

        Args:
        num_players (int): Number of players to load. Defaults to 8.

        Returns:
        list: Randomly selected players.
        """
        players_list = self.model.data_players
        if num_players > len(players_list):
            raise ValueError(
                "Number of players to load exceeds the length of the players list."
            )

        return random.sample(players_list, num_players)
