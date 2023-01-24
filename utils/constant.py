"""
The constant variables are made to have to change only one digit and
avoid any errors.
"""


class Constants:
    NUMBER_OF_DAY: int = 0
    NUMBER_OF_ROUND: int = 4
    NUMBER_OF_PLAYERS: int = 8

    BLITZ: int = 10
    BULLET: int = 3

    @staticmethod
    def reception(var):
        player_reception = f" {var} "
        print(f"\n{player_reception.center(106, ' ')}")

    @staticmethod
    def select_number():
        return input("Select the menu number : ")

    @staticmethod
    def select_choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def enter_information():
        information_decoration = " Enter information "
        print(f"{information_decoration.center(106, '*')}")

    @staticmethod
    def value_error():
        print("Value error.")

    @staticmethod
    def input_error(var):
        print(f"Invalid input: {var}. Please try again.")

    @staticmethod
    def confirmation_menu():
        exit_list = "> 1.Yes  2.No <"
        print(f"\n{exit_list.center(106, '-')}")
