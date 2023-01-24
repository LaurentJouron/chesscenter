"""Management of the tournament organization"""
from utils.constant import Constants
from tournament.view import TournamentView
from tournament.controller import TournamentController
from player.controller import Player


class Tournament:
    def __init__(self):
        self.constants = Constants()
        self.view = TournamentView()
        self.tournament = TournamentController()
        self.player = Player()

    def tournament_menu(self):
        global_tournament = None

        tournament = True
        while tournament:
            """Decoration text reception tournament for in line game."""
            self.constants.reception(" TOURNAMENT RECEPTION ")
            self.constants.select_choice()
            self.view.tournament_menu()

            """
            Input the number choice of the tournament menu.
            """
            menu_number = self.constants.select_number()
            choice_menu = int(menu_number)

            if choice_menu >= 6:
                self.constants.value_error()

            if choice_menu == 1:
                """Decoration text creation tournament for in line game."""
                self.constants.reception(" TOURNAMENT CREATION ")
                self.constants.enter_information()

                """
                Input information for create tournament
                and assign the global variable.
                """
                global_tournament = self.tournament.new_tournament()

            elif choice_menu == 2:
                """Decoration to add players tournament for in line game."""
                self.constants.reception(" APPEND TOURNAMENT PLAYERS ")
                self.constants.enter_information()

                """
                Enter the players information for add to the tournament.
                :parameter global variable tournament.
                """
                self.tournament.append_player(global_tournament)

            elif choice_menu == 3:
                """Decoration text display all players in this tournament."""
                self.constants.reception(" ALL PLAYERS IN TOURNAMENT ")
                self.view.list_player()

                """
                Display all players in this tournament.
                :parameter global variable tournament.
                """
                print(self.tournament.get_players_list(tournament))

            elif choice_menu == 4:
                """Decoration text delete player in this tournament."""
                self.constants.reception(" REMOVE PLAYERS TOURNAMENT ")
                self.constants.enter_information()

                """
                Input information for delete player in this tournament.
                :parameter global variable tournament.
                """
                self.tournament.remove_player(tournament)

            elif choice_menu == 5:
                tournament = False
