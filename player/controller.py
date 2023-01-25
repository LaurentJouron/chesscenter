"""Tournament player registration management."""
from utils.constant import Constants
from player.view import PlayerView
from player.model import PlayerModel as Model


class Player:
    """Control information player you need to organize a tournament."""
    def __init__(self):
        self.constants = Constants()
        self.view = PlayerView()

    def create(self):
        """Imports view data, imports model data and compares accuracy."""
        self.constants.reception(" PLAYER CREATION ")
        self.constants.enter_information()

        first_name = self.view.get_first_name()
        last_name = self.view.get_last_name()
        birthday = self.view.get_birthday()
        gender = self.view.get_gender()
        ranking = self.view.get_ranking()

        player = Model(first_name=first_name,
                       last_name=last_name,
                       birthday=birthday,
                       gender=gender,
                       ranking=ranking)
        player.save()
        self.view.player_register(f"{first_name} {last_name}")
        return player

    def get_all(self):
        """Deserializes the database data in list comprehension."""
        self.constants.reception(" ALL PLAYERS IN LIST ")
        self.view.display_all_players()
        return Model.get_all()

    def remove(self):
        """Removes an item from the list"""
        self.constants.reception(" ALL PLAYERS IN LIST ")
        self.constants.enter_information()

        first_name = self.view.get_first_name()
        last_name = self.view.get_last_name()
        player = Model(first_name=first_name,
                       last_name=last_name)
        player.remove()
        self.view.remove_confirmation(first_name, last_name)

    def get_one_player(self):
        """Get a player with his first-name"""
        first_name = self.view.get_first_name()
        last_name = self.view.get_last_name()
        player = Model.get_one_player(first_name=first_name,
                                      last_name=last_name)
        return player["first_name"], \
            player["last_name"], \
            player["birthday"], \
            player["gender"], \
            player["ranking"]

    def remove_player_list(self):
        """Removes an item from the list"""
        first_name = self.view.get_first_name()
        last_name = self.view.get_last_name()
        return Model(first_name=first_name,
                     last_name=last_name)
