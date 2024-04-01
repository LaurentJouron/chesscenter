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

    def tournament_data(self):
        name = self.get_name()
        location = self._get_string("Place of the tournament: ")
        start = self._get_valid_date(
            "Enter start date (YYYY.MM.DD): ", future_date=True
        )
        start_date = self.convert(start)
        end = self._get_valid_date(
            "Enter end date (YYYY.MM.DD): ",
            start_date=start,
            future_date=False,
        )
        end_date = self.convert(end)
        description = self._get_string("Enter a comment if needed: ")
        return {
            "name": name,
            "location": location.capitalize(),
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
        }

    def display_new_tournament(self):
        """
        Displaying an upside down output message for using pyfiglet
        """
        self._display_pyfiglet("tnemanruot weN")
