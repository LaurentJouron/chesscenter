from utils.constant import Constants
from player.view import PlayerView
from player.controller import Player


class PlayerMenu:
    def __init__(self):
        self.player = Player()
        self.view = PlayerView()
        self.constants = Constants()

    def player_menu(self):
        players = True
        while players:
            self.constants.reception(" PLAYER RECEPTION ")
            self.constants.select_choice()
            self.view.player_menu()

            choice_menu = int(self.constants.select_number())

            if choice_menu >= 5:
                self.constants.value_error()

            if choice_menu == 1:
                """Input information for create player in data file."""
                self.player.create()

            elif choice_menu == 2:
                """Display all players in data file."""
                print(self.player.get_all())

            elif choice_menu == 3:
                """Input information for delete player in data file."""
                self.player.remove()

            elif choice_menu == 4:
                """Input information for exit the players menu."""
                players = False
