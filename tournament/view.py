"""Enter information for the tournament organization."""
from datetime import date, timedelta
from utils.constant import Constants


class TournamentView:
    def __init__(self):
        self.constants = Constants()

    def name(self) -> str:
        """
        Generate a name tournament.
        Returns:
            str: name
        """
        while True:
            name = input("Enter the tournament name: ").capitalize()
            if not name.isalpha():
                self.constants.input_error(name)
            else:
                return name

    def place(self) -> str:
        """
        Generate place of the tournament.
        Returns:
            str: place
        """
        while True:
            place = input("Place of the tournament: ").capitalize()
            if not place.isalpha():
                self.constants.input_error(place)
            else:
                return place

    @staticmethod
    def start_date():
        """
        Generate the date the tournament begins.
        Returns:
            date: start
        """
        start_date = date.today()
        start_date = start_date.strftime("%A %d %B %Y")
        return start_date

    def end_date(self):
        """
        Tournament end date.
        :arguments:
            date: start date
        Returns:
            str: same day
            or
            date: end date
        """
        self.constants.reception(" NUMBER DAYS ")
        self.constants.select_choice()
        TournamentView.number_of_the_day(self.constants.NUMBER_OF_DAY + 1)
        self.constants.confirmation_menu()
        today = TournamentView.start_date()
        validate = int(self.constants.select_number())

        if validate == 10:
            TournamentView.number_of_the_day(self.constants.NUMBER_OF_DAY + 1)
            end_date = date.today() + timedelta(self.constants.NUMBER_OF_DAY)
            if end_date == date.today():
                return "same day"
        elif validate == 2:
            new_days = TournamentView.how_many_day()
            new_number = int(new_days)
            TournamentView.number_of_the_day(self.constants.NUMBER_OF_DAY)
            end_date = today + timedelta(new_number - 1)
            return end_date.strftime("%A %d %B %Y")

    def number_rounds(self) -> int:
        """
        Generate number of rounds for the tournament.
        Returns:
            int: number of rounds
        """
        self.constants.reception(" NUMBER ROUNDS ")
        self.constants.select_choice()
        TournamentView.number_of_the_rounds(self.constants.NUMBER_OF_ROUND)
        self.constants.confirmation_menu()

        validate = int(self.constants.select_number())
        if validate == 1:
            TournamentView.number_of_the_rounds(self.constants.NUMBER_OF_ROUND)
            return self.constants.NUMBER_OF_ROUND
        if validate == 2:
            new_number = TournamentView.how_many_rounds()
            new_number = int(new_number)
            TournamentView.number_of_the_rounds(new_number)
            return new_number

    def number_players(self) -> int:
        """
        Generate number of player for the tournament.
        Returns:
            int: number of player
        """
        self.constants.reception(" NUMBER PLAYERS ")
        self.constants.select_choice()
        TournamentView.number_of_the_players(self.constants.NUMBER_OF_PLAYERS)
        self.constants.confirmation_menu()
        validate = int(self.constants.select_number())

        if validate == 1:
            TournamentView.number_of_the_players(self.constants.NUMBER_OF_PLAYERS)
            return self.constants.NUMBER_OF_PLAYERS
        if validate == 2:
            new_number = TournamentView.how_many_players()
            new_number = int(new_number)
            TournamentView.number_of_the_players(new_number)
            return new_number

    @staticmethod
    def tournament_menu():
        tournament = "> 1.Create  2.Add player  3.Display player  4.Remove player  5.Quit <"
        print(f"\n{tournament.center(106, '-')}")

    @staticmethod
    def confirmation_of_tournament_creation(name, place, start_date,
                                            end_date, nb_players, nb_rounds):
        """Confirmation phrase of the tournament class."""
        print(f"\nThe {name} chess tournament starts on"
              f" {start_date} at 9:00 am, and end on {end_date} at 6:00 pm.\n"
              f"He takes place in {place}.\n"
              f"It will be played with {nb_players} players in {nb_rounds} rounds.")

    @staticmethod
    def how_many_day():
        return input("\nHow many days ? ")

    @staticmethod
    def number_of_the_day(nb_day):
        print(f"\nThis tournament will play in {nb_day} day(s).")

    @staticmethod
    def how_many_players():
        return input("\nHow many players ? ")

    @staticmethod
    def number_of_the_players(nb_players):
        print(f"\nThis tournament will play with {nb_players} players")

    @staticmethod
    def list_player():
        information_decoration = " All players in the tournament"
        print(f"{information_decoration.center(106, '*')}")

    @staticmethod
    def how_many_rounds():
        return input("\nHow many round ? ")

    @staticmethod
    def number_of_the_rounds(nb_round):
        print(f"\nThis tournament will play in {nb_round} rounds.")

    @staticmethod
    def create_tournament_before_add_players():
        print("You need to create tournament before to add players.")
