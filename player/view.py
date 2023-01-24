"""All views information for the players will participate."""
from datetime import datetime
from utils.constant import Constants


class PlayerView:
    """The player information."""
    def __init__(self):
        self.constants = Constants()

    def get_first_name(self) -> str:
        """Define the first-name of participants.
        Returns:
            str: players first-name """
        while True:
            first_name = input("Please enter the player’s first name: ")
            if not first_name.isalpha():
                self.constants.input_error(first_name)
            else:
                return first_name.capitalize()

    def get_last_name(self) -> str:
        """Define the last_name of participants.
        Returns:
            str: players last-name """
        while True:
            last_name = input("Enter the last name: ").capitalize()
            if not last_name.isalpha():
                self.constants.input_error(last_name)
            else:
                return last_name

    def get_birthday(self) -> str:
        """Define the birthday of participants.
        Returns:
            date: players birthday """
        while True:
            birthday = input("Enter date of birth: ")
            if not birthday.isdigit():
                self.constants.input_error(birthday)
            else:
                birthday = datetime.strptime(birthday, "%d%m%Y"). \
                    strftime("%A %d %B %Y")
                return birthday

    def get_gender(self) -> str:
        """Define the gender of participants.
        Returns:
            str: players gender """
        gender = ""
        while gender != "W" or "M":
            gender = input("Select M for men or W for women: ")
            gender = gender.upper()
            if gender == "W":
                return "woman"
            elif gender == "M":
                return "man"
            else:
                self.constants.input_error(gender)

    def get_ranking(self):
        """Define the ranking of participants.
        Returns:
            int: players national ranking """
        while True:
            ranking = input("Indicate your place in the national ranking: ")
            ranking = int(ranking)
            if not ranking or ranking <= 0:
                self.constants.input_error(ranking)
            else:
                return ranking

    @staticmethod
    def remove_confirmation(first_name, last_name):
        print(f"\n{first_name} {last_name} has been deleted from the list.")

    @staticmethod
    def player_register(full_name):
        print(f'\n{full_name} is register.')

    @staticmethod
    def player_menu():
        player_menu = "> 1.Add  2.Show  3.Remove  4.Quit <"
        print(f"\n{player_menu.center(106, '-')}")

    @staticmethod
    def display_all_players():
        information_decoration = " Display all players in list "
        print(f"{information_decoration.center(106, '*')}")
