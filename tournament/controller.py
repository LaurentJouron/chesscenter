"""Management of the tournament organization"""
from utils.constant import Constants
from tournament.view import TournamentView
from player.controller import Player
from tournament.model import TournamentModel as Model


class TournamentController:
    def __init__(self):
        self.constants = Constants()
        self.view = TournamentView()
        self.player = Player()

    def new_tournament(self):
        """
        imports the data of the views
        and passes these data parameters in the models.
        """
        name = self.view.name()
        place = self.view.place()
        start_date = self.view.start_date()
        end_date = self.view.end_date()
        nb_rounds = self.view.number_rounds()
        nb_players = self.view.number_players()

        new_tournament = Model(name=name,
                               place=place,
                               start_date=start_date,
                               end_date=end_date,
                               nb_rounds=nb_rounds,
                               nb_players=nb_players)
        self.view.confirmation_of_tournament_creation(name, place, start_date, end_date, nb_players, nb_rounds)
        return new_tournament

    def append_player(self, tournament):
        """Returns the players to be added to the tournament list."""
        if tournament is None:
            self.view.create_tournament_before_add_players()
            return
        if tournament != "":
            tournament.append_player(self.player.get_one_player())

    @staticmethod
    def get_players_list(tournament):
        """Display all participants of the tournament."""
        return tournament.get_players_list()

    @staticmethod
    def remove_player(tournament):
        """Remove player un tournament list"""
        tournament.remove_player()
