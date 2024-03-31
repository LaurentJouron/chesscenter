from ..utils.bases.menus import BaseMenu


class TournamentView(BaseMenu):
    tournament_menu: dict = {
        "1": "Get all",
        "2": "Tournament - Player",
        "5": "Quit",
    }
    search_tournament: dict = {
        "1": "By name",
        "2": "By location",
        "3": "By year",
        "5": "Quit",
    }

    def display_new_tournament(self):
        """
        Displaying an upside down output message for using pyfiglet
        """
        self._display_pyfiglet("tnemanruot weN")
