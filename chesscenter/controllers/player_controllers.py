from ..models.player_models import PlayerModel
from ..views.player_views import PlayerView
from ..data.db_id_players import players_id
from operator import attrgetter
from tinydb import Query

view = PlayerView()


class ControllerPlayer:
    def __init__(self, model):
        self.model = PlayerModel

    def check_id_number(self):
        id_number_tested = view.get_player_id_number()

        # Player with no ID

        if int(id_number_tested) == 0:
            return self._extracted_from_check_id_number_22()
        Player = Query()
        results_players_database = PlayerModel.players_database.search(
            Player.id_number == int(id_number_tested)
        )

        # No matching result with the ID entered

        if len(results_players_database) == 0:
            view.return_unknown_id()
            return self._extracted_from_check_id_number_22()
        elif len(results_players_database) == 1:
            t_p = PlayerModel.tournament_players
            results_t_p = t_p.search(Player.id_number == int(id_number_tested))

            # The player is recognized and added to the tournament

            if len(results_t_p) == 0:
                view.return_successful_identification()
                for result in results_players_database:
                    player = PlayerModel.deserialize_player(result)
                    view.print_player(player)
                    print(PlayerView.line)
                    if self < 8:
                        view.announce_next_player()
                return result

            elif len(results_t_p) == 1:
                view.return_player_already_registered()
                return self._extracted_from_check_id_number_22()

    # TODO Rename this here and in `check_id_number`
    def _extracted_from_check_id_number_22(self):
        view.generate_player()
        player = ControllerPlayer.add_player_to_tournament()
        serialized_player = PlayerModel.serialize_player(player)
        PlayerModel.save_db_players(serialized_player)
        return serialized_player

    def add_player_to_database():
        player_features = view.get_player_inputs()
        player_index = len(PlayerModel.players_database)
        id_number = players_id[player_index]
        player = PlayerModel(
            player_features[0],
            player_features[1],
            id_number,
            player_features[2],
            player_features[3],
            player_features[4],
        )
        view.print_player(player)
        return player

    def add_player_to_all_players_database():
        player = ControllerPlayer.add_player_to_database()
        view.confirm_player_addition_to_all_players_database()
        print(view.line)
        return player

    def add_player_to_tournament():
        """A function to add a player to a tournament."""

        player = ControllerPlayer.add_player_to_database()
        view.confirm_player_addition_to_tournament()
        print(PlayerView.line)
        return player

    def print_player_ranking():
        view.get_player_ranking()
        player_name = PlayerView.get_player_name()
        for i in range(8):
            if player_name in PlayerModel.tournament_players[i].last_name:
                player_ranking = PlayerModel.tournament_players[i].ranking
                return view.print_player_ranking(player_name, player_ranking)

    def announce_new_rankings():
        view.set_new_rankings()

    def recap_ranking(self, id_number, ranking):
        view.print_player_new_ranking(self, id_number, ranking)

    def set_new_rankings(self):
        new_ranking = view.change_player_ranking()
        id_number = self["id_number"]
        Player = Query()
        PlayerModel.players_database.update(
            {"ranking": new_ranking}, Player.id_number == id_number
        )
        view.confirm_ranking_change()
        return new_ranking

    def change_ranking():
        player = ControllerPlayer.get_player()
        if player is not None:
            player = player[0]
            new_ranking = view.change_player_ranking()
            id_number = player["id_number"]
            Player = Query()
            PlayerModel.players_database.update(
                {"ranking": new_ranking}, Player.id_number == id_number
            )
            view.confirm_ranking_change()

    def take_fourth(self):
        """A function to return the third element of a list."""

        return self[3]

    def slice_results(list_to_slice):
        """A function to split a list into 40 chunks."""

        return [
            list_to_slice[i : i + 39] for i in range(0, len(list_to_slice), 39)
        ]

    def see_chunks_items(self):

        if len(self) == 0:
            view.return_no_player()

        if len(self) <= 40:
            for chunk in self:
                view.print_sorted_players(chunk)

        else:
            chunks = ControllerPlayer.slice_results(self)
            for elt in chunks[0]:
                view.print_sorted_players(elt)
            i = 1
            while i < len(chunks):
                see_more = view.see_more_results()
                if see_more in "yY":
                    for elt in chunks[i]:
                        view.print_sorted_players(elt)
                    i += 1
                elif see_more in "nN":
                    break

        return len(self)

    def sort_players_by_ranking(self):
        deserialized_players = []
        for player in self:
            deserialized_player = PlayerModel.deserialize_player(player)
            deserialized_players.append(deserialized_player)
        sorted_players = sorted(
            deserialized_players, key=attrgetter("ranking"), reverse=True
        )
        chunks = ControllerPlayer.see_chunks_items(sorted_players)

    def sort_all_players_by_ranking():
        """A function to sort all the players by ranking."""

        view.print_all_players_by_ranking()
        ControllerPlayer.sort_players_by_ranking(PlayerModel.players_database)

    def sort_players_by_last_name(self):
        """A function to sort the players of a tournament by last name."""

        deserialized_players = []
        for player in self:
            deserialized_player = PlayerModel.deserialize_player(player)
            deserialized_players.append(deserialized_player)
        sorted_players = sorted(
            deserialized_players, key=attrgetter("last_name")
        )
        ControllerPlayer.see_chunks_items(sorted_players)

    def sort_all_players_by_last_name():
        """A function to sort all the players by last name."""

        view.print_all_players_by_last_name()
        database = PlayerModel.players_database
        ControllerPlayer.sort_players_by_last_name(database)

    def return_search_results(self):
        Player = Query()

        view.print_number_of_results(self)

        if len(self) == 1:
            searched_player = self[0]

        elif len(self) > 1:
            for i, player in enumerate(self, start=1):
                view.print_players_options(player, i)
            player_chosen = view.choose_player(self)
            searched_player = self[int(player_chosen) - 1]

        serialized_player = PlayerModel.players_database.search(
            Player.id_number == searched_player["id_number"]
        )
        deserialized_player = PlayerModel.deserialize_player(searched_player)
        print(deserialized_player)
        return serialized_player

    def search_player_with_last_name():
        Player = Query()

        last_name = view.search_last_name()
        players = PlayerModel.players_database.search(
            Player.last_name == last_name
        )

        if len(players) == 0:
            view.return_no_player()

        elif len(players) > 0:
            return ControllerPlayer.return_search_results(players)

    def search_player_with_id_number():
        Player = Query()

        id_number = view.search_id_number()
        players = PlayerModel.players_database.search(
            Player.id_number == id_number
        )

        if len(players) == 0:
            view.return_no_player()

        elif len(players) > 0:
            return ControllerPlayer.return_search_results(players)

    def get_player():
        option_number = view.search_player()

        if option_number == "1":
            return ControllerPlayer.search_player_with_last_name()
        elif option_number == "2":
            return ControllerPlayer.search_player_with_id_number()
