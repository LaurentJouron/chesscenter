from ..utils.bases.controllers import BaseController

# from models.player_models import PlayerModel
# from controllers.controller_tournament import ControllerTournament
from ..controllers.player_controllers import PlayerController
from ..views.home_views import HomeView
from ..utils.constants import CONFIRMATION_MENU

view = HomeView()


class HomeController(BaseController):
    def run(self):
        view.welcome_game()
        view.game_instruction()
        while True:
            choice = view.display_menu(view.home_menu)
            if choice == "1":
                print("Generate tournois")

            elif choice == "2":
                return PlayerController()

            elif choice == "3":
                print("Tournament")
                # return TournamentController()

            elif choice == "4":
                print("round")

            elif choice == "5":
                return ExitController()


class ExitController(BaseController):
    def run(self):
        view.exit_game()
        choice = view.display_menu(CONFIRMATION_MENU)
        return None if choice == "1" else HomeController()
