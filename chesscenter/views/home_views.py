from ..utils.bases.menus import BaseMenu


class HomeView(BaseMenu):
    home_menu: dict = {
        "1": "Generate tournament",
        "2": "Player",
        "3": "tournament",
        "4": "Tour",
        "5": "Quit",
    }

    def display_menu(self, menu_dict):
        """
        Display a menu and get user's choice.

        Args:
            menu_dict (dict): The menu options.

        Returns:
            str: The user's choice.
        """
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def welcome_game(self):
        """
        Displaying an upside down welcome message for using pyfiglet
        """
        self._display_pyfiglet("retneC - ssehC")

    def game_instruction(self):
        """
        Display game instructions.
        """
        self._space_presentation("Please follow the instructions below")

    def exit_game(self):
        """
        Displaying an upside down output message for using pyfiglet
        """
        self._display_pyfiglet("retnec ssehc tixE")

    def good_by(self):
        """
        Display a farewell message.
        """
        self._space_presentation("Good day and see you soon...\n")
