from datetime import datetime
from ..utils.bases.views import BaseView
from ..utils.bases.menus import BaseMenu


class PlayerView(BaseMenu, BaseView):
    gender_menu: dict = {"1": "Male", "2": "Female"}
    player_menu: dict = {
        "1": "Get all",
        "2": "Change rank",
        "3": "Create",
        "5": "Return",
    }
    search_player: dict = {
        "1": "By rank",
        "2": "By last name",
        "5": "Return",
    }

    def get_data(self):
        id_number = self.get_player_id()
        last_name = self._get_string("Enter the last name: ")
        first_name = self._get_string("Please enter the player’s first name: ")
        birthday = self._get_valid_date("Enter the birth date (ddmmyyyy): ")
        gender = self.get_gender()
        birthday = self.convert(birthday)
        rank = self.get_rank()
        return {
            "id_number": id_number,
            "first_name": first_name.capitalize(),
            "last_name": last_name.capitalize(),
            "birthday": birthday,
            "gender": gender,
            "rank": rank,
        }

    # Presentation
    def display_reception(self):
        """
        Displaying an upside down welcome player message for using pyfiglet
        """
        self._display_pyfiglet("noitpecer reyalP")

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

    def get_player_id(self):
        return self._get_int("Enter player ID number:")

    def get_gender(self):
        while True:
            choice = self.display_menu(self.gender)
            if choice in self.gender:
                return self.gender[choice]

    def get_player(self):
        self._stars_presentation(" NEW PLAYER ")

        last_name = input("Enter player's last name: ")
        while not all(char.isalpha() or char.isspace() for char in last_name):
            print("Please enter a valid last name.")
            last_name = input("Enter player's last name: ")
            continue

        first_name = input("Enter player's first name: ")
        while not all(char.isalpha() or char.isspace() for char in first_name):
            print("Please enter a valid first name.")
            first_name = input("Enter player's first name: ")
            continue

        year_of_birth = input("Enter player's year of birth (YYYY): ")
        current_year = datetime.now().year
        if year_of_birth.isdigit() is True:
            while not 100 > current_year - int(year_of_birth) > 18:
                print("Enter a valid date of birth")
                year_of_birth = input("Enter player's year of birth (YYYY): ")
                if year_of_birth.isdigit() is True:
                    continue
                else:
                    break
        year_of_birth = str(year_of_birth)
        month_of_birth = input("Enter player's month of birth (MM): ")
        if len(month_of_birth) == 1:
            month_of_birth = f"0{month_of_birth}"
        day_of_birth = input("Enter player's day of birth (DD): ")
        if len(day_of_birth) == 1:
            day_of_birth = f"0{day_of_birth}"
        birth_date = f"{year_of_birth}-{month_of_birth}-{day_of_birth}"
        while True:
            try:
                birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Please enter a valid birth date (YYYY.MM.DD)")
                year_of_birth = input("Enter player's year of birth (YYYY): ")
                month_of_birth = input("Enter player's month of birth (MM): ")
                day_of_birth = input("Enter player's day of birth (DD): ")
                birth_date = f"{year_of_birth}-{month_of_birth}-{day_of_birth}"
        date_tuple = (year_of_birth, month_of_birth, day_of_birth)
        birth_date = ".".join(date_tuple)

        gender = input("Enter player's gender (M/F): ")
        while str(gender) not in "mMfF" or gender.isalpha() is False:
            print("Please enter a valid gender (M/F).")
            gender = input("Enter player's gender (M/F): ")
            continue

        ranking = input("Enter player's ranking: ")
        while not isinstance(ranking, float):
            try:
                ranking = float(ranking)
                break
            except Exception:
                print("Please enter a valid ranking (positive float).")
                ranking = input("Enter player's ranking: ")

        score = 0

        print(ViewPlayer.line)
        return (last_name, first_name, birth_date, gender, ranking, score)

    def generate_player(self):
        self._display_message("Generating new player...\n")

    def return_unknown_id(self):
        self._display_message("ID number not recognized")

    def return_successful_identification(self):
        self._success_message()
        self._display_message("\nPlayer details:\n")

    def return_player_already_registered(self):
        self._display_message("Player already registered in tournament")

    def announce_next_player(self):
        self._display_message("\nNext player:\n")

    def print_player(self, player):
        self._display_message(f"Player {player.id_number} \n")
        self._display_message(
            f"- Player name : {player.first_name} {player.last_name}"
        )
        self._display_message(f"- Gender : {player.gender}")
        self._display_message(
            f"- Date of birth (YYYY.MM.DD) : {player.birth_date}"
        )
        self._display_message(f"- Current ranking : {player.ranking}")
        self._display_message(f"- Score : {player.score}\n")

    def confirm_player_addition_to_all_players_database(self):
        self._display_message("Player added to players database")

    def confirm_player_addition_to_tournament(self):
        self._display_message("Player added to tournament")

    def set_new_rankings(self):
        self._display_message("NEW RANKINGS\n")
        self._display_message("Set new ranking for each player")

    def change_player_ranking(self):
        return self._get_float("Enter new rank: ")

    def confirm_ranking_change(self):
        self._success_message()

    def print_player_new_ranking(self, last_name, id_number, new_ranking):
        self.__drew_presentation("-")
        self._display_message(f"- Player {id_number} : {last_name}")
        self._display_message(f"- Ranking : {new_ranking}")
        self.__drew_presentation("-")

    def print_tournament_players_by_last_name(self):
        self._display_message("Tournament players (sorted by last name)")

    def print_tournament_players_by_ranking(self):
        self._display_message("Tournament players (sorted by ranking)")

    def print_all_players_by_last_name(self):
        self._display_message("Database players (sorted by last name)\n")

    def print_sorted_players(self, player):
        message = (
            f"Player {player.id_number} : "
            f"{player.first_name} {player.last_name} - "
            f"Ranking: {player.ranking}"
        )
        self._display_message(message)

    def see_more_results(self):
        return self._get_string(
            "\nSee next results ? (Y/N)\n",
            validator=lambda char: char.upper() in "YN",
        )

    def print_all_players_by_ranking(self):
        self._display_message("Database players (sorted by ranking)\n")

    def print_number_of_results(self, results):
        self._display_message(f"Number of results: {len(results)}\n")

    def print_players_options(self, player, i):
        message = (
            f"[{i}] Player {player['id_number']} : "
            f"{player['first_name']} {player['last_name']}"
        )
        self._display_message(message)

    def choose_player(self, players):
        while True:
            player_chosen = self._get_int("\nChoose a player number: ")
            if player_chosen > 0 and player_chosen <= len(players):
                return player_chosen
            else:
                self._value_error(player_chosen)

    def search_last_name(self):
        while True:
            last_name = self._get_string("\nEnter player last name: ")
            if last_name.isalpha():
                return last_name
            else:
                self._value_error("Only contain alphabetical characters.")

    def search_id_number(self):
        while True:
            id_number = self._get_int("\nEnter player ID number: ")
            if id_number > 0:
                return id_number
            else:
                self._value_error("ID number should be a positive integer.")

    def return_no_player(self):
        self._display_message("\nNo player found\n")

    def search_player(self):
        while True:
            option_number = self._get_string(
                "\nSearch player (Enter option number): \n\n"
                "By last name [1]\nBy ID number [2]\n\n"
            )
            if option_number in "12" and option_number != "":
                return option_number
            else:
                self._value_error("It's not valid option number (1 or 2).")
