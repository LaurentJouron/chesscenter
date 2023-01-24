"""Entry point."""
from chesscenter.view import ChessView
from tournament.menu import Tournament
from player.menu import PlayerMenu
from utils.constant import Constants


class ChessCenter:
    def __init__(self):
        self.view = ChessView()
        self.constants = Constants()
        self.player = PlayerMenu()
        self.tournament = Tournament()
    """Decoration text when opening the application."""

    def play(self):
        self.view .welcome()
        self.view .instruction()

        reception = True
        while reception:

            """Decoration text reception for in line game"""
            self.constants.reception(" RECEPTION ")
            self.constants.select_choice()
            self.view.start_menu()

            """Input the number choice of the reception menu"""
            input_menu = int(self.constants.select_number())

            if input_menu >= 5:
                self.constants.value_error()

            if input_menu == 1:
                """Reception of player menu"""
                self.player.player_menu()

            elif input_menu == 2:
                """Reception of tournament menu"""
                self.tournament.tournament_menu()

            elif input_menu == 4:
                """exit game"""
                self.constants.reception(" EXIT CHESS CENTER ")
                self.view.exiting_program()
                self.constants.confirmation_menu()

                """Input the number choice of the exit menu"""
                exit_menu = int(self.constants.select_number())

                if exit_menu >= 3:
                    self.constants.value_error()
                if exit_menu == 2:
                    reception = True
                elif exit_menu == 1:
                    reception = False
