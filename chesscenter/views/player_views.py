import random
from ..utils.bases.views import BaseView
from ..utils.bases.menus import BaseMenu
from ..utils.bases.date import BaseDate


class PlayerView(BaseDate, BaseMenu, BaseView):
    gender_menu: dict = {"1": "Male", "2": "Female"}
    player_menu: dict = {
        "1": "Generate",
        "2": "Get all",
        "3": "Create",
        "4": "Search",
        "5": "Return",
    }
    search_player: dict = {
        "1": "By rank",
        "2": "By last name",
        "3": "By ID",
        "5": "Return",
    }

    def get_data(self):
        id_number = random.randint(100000, 999999)
        last_name = self._get_string("Enter the last name: ")
        first_name = self._get_string("Please enter the player’s first name: ")
        birthday = self._get_valid_date("Enter the birth date YYYY.MM.DD: ")
        gender = self.get_gender()
        birthday = self.convert(birthday)
        rank = self._get_int("Please enter the rank: ")
        return {
            "id_number": id_number,
            "first_name": first_name.capitalize(),
            "last_name": last_name.capitalize(),
            "birthday": birthday,
            "gender": gender,
            "rank": rank,
        }

    # Presentation
    def get_gender(self):
        while True:
            choice = self.display_menu(self.gender_menu)
            if choice in self.gender_menu.keys():
                return self.gender_menu[choice]
            else:
                self._value_error(choice)

    def display_reception(self):
        """
        Displaying an upside down welcome player message for using pyfiglet
        """
        self._display_pyfiglet("noitpecer reyalP")

    def display_generate(self):
        """
        Displaying an upside down generate player message for using pyfiglet
        """
        self._display_pyfiglet("etareneg reyalP")

    def display_creation(self):
        """
        Displaying an upside down creation player message for using pyfiglet
        """
        self._display_pyfiglet("noitaerc reyalP")

    def player_register(self, var):
        print(f"\nPlayer {var} is registered.")

    def display_details(self):
        """
        Displaying an upside down details player message for using pyfiglet
        """
        self._display_pyfiglet("sliated reyalP")

    def get_player_id(self):
        return self._get_int("Please enter the player ID: ")

    def get_player_rank(self):
        return self._get_int("Please enter the player rank: ")

    def get_player_lastname(self):
        return self._get_string("Please enter the player lastname: ")

    def display_player(self, player):
        print(player)

    def enter_information(self):
        self._enter_information()

    def display_menu(self, menu_dict):
        """
        Display a menu and get user's choice.

        Args:
            menu_dict (dict): The menu options.

        Returns:
            str: The user's choice.
        """
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)
