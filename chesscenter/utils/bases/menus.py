from chesscenter.utils.bases.views import BaseView


class BaseMenu(BaseView):
    def _display_menu(self, menu_dict):
        """
        Display a menu and return the user's choice.

        Args:
            menu_dict (dict): A dictionary of menu options.

        Returns:
            None
        """
        menu_options = " | ".join(
            [f" {keys}. {value} " for keys, value in menu_dict.items()]
        )
        return self._star_presentation(menu_options)

    def _response_menu(self, menu_dict):
        """
        Collect and validate the user's choice from the menu.

        Args:
            menu_dict (dict): A dictionary of menu options.

        Returns:
            str: The user's choice.
        """
        choice = self._select_number()
        return choice if choice in menu_dict else self._message_error(choice)
