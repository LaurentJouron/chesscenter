from datetime import datetime
from ..utils.bases.views import BaseView
from ..utils.bases.views import BasePlayer
from ..utils.bases.menus import BaseMenu


class ViewPlayer(BasePlayer, BaseMenu, BaseView):
    gender: dict = {"1": "Male", "2": "Female"}

    def get_data(self):
        self._stars_presentation(" NEW PLAYER ")
        id_number = self.get_player_id()
        first_name = self._get_string("Please enter the player’s first name: ")
        last_name = self._get_string("Enter the last name: ")
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

    def get_gender(self):
        while True:
            choice = self.display_menu(self.gender)
            if choice in self.gender:
                return self.gender[choice]

    # def get_player_id(self):
    #     player_id = input("Enter player's ID number (if None, enter 0): ")
    #     while not isinstance(player_id, int):
    #         try:
    #             player_id = int(player_id)
    #             break
    #         except Exception:
    #             print("Please enter a valid ID number.")
    #             player_id = input(
    #                 "Enter player's ID number (if None, enter 0): "
    #             )
    #     return player_id

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

    @staticmethod
    def generate_player():
        print("Generating new player...\n")

    @staticmethod
    def return_unknown_id():
        print("ID number not recognized")

    @staticmethod
    def return_successful_identification():
        print("\nIdentification successful")
        print("\nPlayer details:\n")

    @staticmethod
    def return_player_already_registered():
        print("Player already registered in tournament")

    @staticmethod
    def announce_next_player():
        print("\nNext player:\n")

    @staticmethod
    def print_player(player):
        print(f"Player {player.id_number} \n")
        print(f"- Player name : {player.first_name} {player.last_name}")
        print(f"- Gender : {player.gender}")
        print(f"- Date of birth (YYYY.MM.DD) : {player.birth_date}")
        print(f"- Current ranking : {player.ranking}")
        print(f"- Score : {player.score}\n")

    @staticmethod
    def confirm_player_addition_to_all_players_database():
        print("Player added to players database")

    @staticmethod
    def confirm_player_addition_to_tournament():
        print("Player added to tournament")

    @staticmethod
    def set_new_rankings():
        print("NEW RANKINGS\n")
        print("Set new ranking for each player")

    @staticmethod
    def change_player_ranking():
        new_ranking = input("\nEnter new ranking: ")
        while not isinstance(new_ranking, float):
            try:
                new_ranking = float(new_ranking)
            except Exception:
                print("Please enter a valid ranking (positive float).")
                new_ranking = input("\nEnter new ranking: ")
                continue
        return new_ranking

    @staticmethod
    def confirm_ranking_change():
        print("\nRanking successfully changed !\n")

    @staticmethod
    def print_player_new_ranking(last_name, id_number, new_ranking):
        print(ViewPlayer.line)
        print(f"- Player {id_number} : {last_name}")
        print(f"- Ranking : {new_ranking}")
        print(ViewPlayer.line)

    @staticmethod
    def print_tournament_players_by_last_name():
        print("Tournament players (sorted by last name)")

    @staticmethod
    def print_tournament_players_by_ranking():
        print("Tournament players (sorted by ranking)")

    @staticmethod
    def print_all_players_by_last_name():
        print("Database players (sorted by last name)\n")

    @staticmethod
    def print_sorted_players(player):
        print(
            f"Player {player.id_number} : {player.first_name} {player.last_name} - Ranking: {player.ranking}"
        )

    @staticmethod
    def see_more_results():
        see_more = input("\nSee next results ? (Y/N)\n")
        while see_more not in "yYnN" or see_more in "":
            see_more = input("\nSee next results ? (Y/N)\n")
            continue
        return see_more

    @staticmethod
    def print_all_players_by_ranking():
        print("Database players (sorted by ranking)\n")

    @staticmethod
    def print_number_of_results(results):
        print(f"\nNumber of results: {len(results)}\n")

    @staticmethod
    def print_players_options(player, i):
        print(
            f"[{i}] Player {player['id_number']} : {player['first_name']} {player['last_name']}"
        )

    @staticmethod
    def choose_player(players):
        player_chosen = input("\nChoose number to select a player\n")
        while not isinstance(player_chosen, int):
            try:
                player_chosen = int(player_chosen)
                while player_chosen not in range(1, len(players) + 1):
                    player_chosen = input("Choose number to select a player\n")
                    continue
                break
            except Exception:
                player_chosen = input("\nChoose number to select a player\n")
        return int(player_chosen)

    @staticmethod
    def search_last_name():
        last_name = input("\nEnter player last name: ")
        while last_name.isalpha() is not True:
            print("Value Error.")
            last_name = input("\nEnter player last name: ")
            continue
        return last_name

    @staticmethod
    def search_id_number():
        id_number = input("\nEnter player ID number: ")
        while not isinstance(id_number, int):
            try:
                id_number = int(id_number)
                break
            except Exception:
                id_number = input("\nEnter player ID (positive number): ")
                continue
        return id_number

    @staticmethod
    def return_no_player():
        print("\nNo player found\n")

    @staticmethod
    def search_player():
        option_number = input(
            "\nSearch player (Enter option number): \n\nBy last name [1]\nBy ID number [2]\n\n"
        )
        while option_number not in "12" or option_number in "":
            option_number = input(
                "Search player (Enter option number): \n\nBy last name [1]\nBy ID number [2]\n"
            )
            continue
        return option_number
