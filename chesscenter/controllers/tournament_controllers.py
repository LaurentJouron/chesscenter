from datetime import datetime
from tinydb import Query
import re
from ..models.player_models import PlayerModel
from ..models.tournament_models import TournamentModel
from ..models.match_models import MatchModel
from ..models.round_models import RoundModel
from ..views.tournament_views import TournamentView
from .player_controllers import PlayerController
from .match_controllers import MatchController
from .round_controllers import RoundController


view = TournamentView()


class ControllerTournament:
    def __init__(self):
        self.model = TournamentModel
        self.player_model = PlayerModel
        self.match_model = MatchModel
        self.round_model = RoundModel
        self.player_controller = PlayerController()
        self.round_controller = RoundController()
        self.match_controller = MatchController()

    def print_tournament_inputs():
        tournament_inputs = view.get_tournament_inputs()
        view.start_tournament(tournament_inputs[0], tournament_inputs[1])
        return tournament_inputs

    def start_tournament():
        start_date = datetime.now().replace(microsecond=0)
        return start_date

    def introduce_players():
        return view.enter_tournament_players()

    def generate_pairs(round_pairs):
        view.announce_round_matches()
        i = 1
        while i < 5:
            first_player = round_pairs[i - 1][0].last_name
            first_id = round_pairs[i - 1][0].id_number
            second_player = round_pairs[i - 1][1].last_name
            second_id = round_pairs[i - 1][1].id_number
            view.print_pairs(
                i, ((first_player, first_id), (second_player, second_id))
            )
            i += 1

    def end_tournament():
        end_date = datetime.now().replace(microsecond=0)
        return end_date

    def print_ending_message():
        return view.print_ending_message()

    def generate_new_tournament(self):
        # Step 1 : Starting a tournament

        tournament_inputs = ControllerTournament.print_tournament_inputs()
        start_date = ControllerTournament.start_tournament()

        # Step 2: Adding 8 players to the tournament

        ControllerTournament.introduce_players()

        self.player_model.tournament_players.truncate()

        for i in range(1, 9):
            player = self.player_controller.check_id_number(i)
            self.player_model.save_tournament_player(player)

        self.model.rounds_list = []
        pairs_list = []

        deserialized_players = []

        for player in self.player_model.tournament_players:
            deserialized_player = self.player_model.deserialize_player(player)
            deserialized_players.append(deserialized_player)

        # Step 3: Starting a loop of 4 rounds

        deserialized_rounds = []

        for i in range(1, 5):

            # Step 4: Starting a round

            start_date = self.round_controller.start_round(i)

            # Step 5: Generating matches according to Swiss-pairing algorithm

            if len(self.model.rounds_list) == 0:
                round_pairs = self.model.generate_pairs_by_ranking(
                    deserialized_players
                )

                # Optional section to print the round pairs
                # And visualize the functioning of Swiss-pairing algorithm

                print("Round pairs\n")
                print(round_pairs)
                print("\n")

                # End of section

                ControllerTournament.generate_pairs(round_pairs)
                pairs_list.extend(round_pairs)

            elif len(self.model.rounds_list) in range(1, 5):
                round_pairs = self.model.generate_pairs_by_score(
                    self.model, deserialized_players, pairs_list
                )

                # Optional section to print the round pairs
                # And visualize the functioning of Swiss-pairing algorithm

                print("Round pairs\n")
                print(round_pairs)
                print("\n")

                # End of section

                ControllerTournament.generate_pairs(round_pairs)
                pairs_list.extend(round_pairs)

            print(view.star_line)

            # Step 6 : Playing the matches of the round

            deserialized_matches = []

            for i in range(0, 4):

                first_player = round_pairs[i][0]
                second_player = round_pairs[i][1]

                self.match_controller.start_match(first_player, second_player)
                match = self.match_controller.print_winner_and_score(
                    first_player, second_player
                )

                serialized_match = self.match_model.serialize_match(match)
                self.round_model.list_of_matches.append(serialized_match)

                deserialized_match = self.match_model.deserialize_match(
                    serialized_match
                )
                deserialized_matches.append(deserialized_match)

            # Step 7 : Ending the round before starting the next one

            end_date = self.round_controller.end_round()

            self.round_controller.print_round_results(
                i, start_date, end_date, deserialized_matches
            )

            round = self.round_model(
                deserialized_matches, start_date, end_date
            )

            deserialized_rounds.append(round)

            serialized_round = self.round_model.serialize_round(round)

            round_serialized_matches = []
            round_deserialized_matches = serialized_round["matches"]
            for match in round_deserialized_matches:
                serialized_match = self.match_model.serialize_match(match)
                round_serialized_matches.append(serialized_match)
            serialized_round["matches"] = round_serialized_matches

            self.model.rounds_list.append(serialized_round)

            self.round_controller.list_of_matches = []

        # Step 8 : Ending the tournament and printing the results

        end_date = ControllerTournament.end_tournament()
        tournament_players_names = []

        self.round_controller.number_of_rounds = 0

        ControllerTournament.print_ending_message()

        self.player_controller.announce_new_rankings()

        for player in self.player_model.tournament_players:
            self.player_controller.recap_ranking(
                player["last_name"], player["id_number"], player["ranking"]
            )
            new_ranking = self.player_controller.set_new_rankings(player)
            player_name = player["last_name"]
            player_id_number = player["id_number"]
            tournament_players_names.append(
                (player_name, player_id_number, new_ranking)
            )

        view.print_tournament_results(
            tournament_inputs[0],
            tournament_inputs[1],
            start_date,
            end_date,
            tournament_inputs[2],
            tournament_inputs[3],
            tournament_players_names,
            deserialized_rounds,
        )

        tournament = self.model(
            tournament_inputs[0],
            tournament_inputs[1],
            start_date,
            end_date,
            tournament_inputs[2],
            tournament_inputs[3],
            tournament_players_names,
        )

        tournament.rounds = self.model.rounds_list

        serialized_tournament = self.model.serialize_tournament(tournament)

        self.model.save_tournament_to_tournaments_database(
            serialized_tournament
        )

    def take_third(elem):
        return elem[2]

    def order_players_by_ranking(database):
        players_to_sort = database["players_list"]
        players_sorted_by_ranking = sorted(
            players_to_sort, key=ControllerTournament.take_third, reverse=True
        )
        view.order_players_by_ranking(players_sorted_by_ranking)

    def order_players_by_last_name(database):
        players_sorted_by_last_name = sorted(database["players_list"])
        view.order_players_by_last_name(players_sorted_by_last_name)

    def print_matching_results(results):
        # The user selects a tournament among the matching tournaments

        if len(results) == 1:
            search_result = results[0]

        elif len(results) > 1:
            tournament_choice = view.choose_tournament(results)
            search_result = results[tournament_choice - 1]
            print("\n")

        # The user can print the player of the tournament selected.
        # The players can be ordered by ranking or by last name.

        players_sorted = view.define_sorting_option()

        # The players are ordered by ranking

        if players_sorted in "aA":
            ControllerTournament.order_players_by_ranking(search_result)

        # The players are ordered by last name

        elif players_sorted in "bB":
            ControllerTournament.order_players_by_last_name(search_result)

    def search_tournament_by_name(self):
        Tournament = Query()
        name = view.enter_tournament_name()
        name = name.title()
        results = self.model.tournaments_database.search(
            Tournament.name == name
        )
        if len(results) == 0:
            view.return_no_tournament()
        elif len(results) > 0:
            view.print_number_of_results(len(results))
            ControllerTournament.see_chunks_items(results)
            ControllerTournament.print_matching_results(results)

    def search_tournament_by_location(self):
        Tournament = Query()
        location = view.enter_tournament_location()
        location = location.capitalize()
        results = self.model.tournaments_database.search(
            Tournament.location == location
        )
        if len(results) == 0:
            view.return_no_tournament()
        elif len(results) > 0:
            view.print_number_of_results(len(results))
            ControllerTournament.see_chunks_items(results)
            ControllerTournament.print_matching_results(results)

    def search_tournament_by_year(self):
        year = view.enter_tournament_year()
        results = []
        number_of_results = 0
        for tournament in self.model.tournaments_database:
            if re.match(year, tournament["start_date"]):
                number_of_results += 1
                results.append(tournament)
        if number_of_results == 0:
            view.return_no_tournament()
        elif number_of_results > 0:
            view.print_number_of_results(len(results))
            ControllerTournament.see_chunks_items(results)
            ControllerTournament.print_matching_results(results)

    def get_tournament():
        choice = view.define_search_criteria()

        if choice in "aA":
            ControllerTournament.search_tournament_by_name()

        elif choice in "bB":
            ControllerTournament.search_tournament_by_location()

        elif choice in "cC":
            ControllerTournament.search_tournament_by_year()

    def slice_results(list_to_slice):
        return [
            list_to_slice[i : i + 9] for i in range(0, len(list_to_slice), 9)
        ]

    def see_chunks_items(chunked_list):
        if len(chunked_list) == 0:
            view.return_no_tournament()

        elif len(chunked_list) > 0 and len(chunked_list) <= 9:
            i = 1
            for chunk in chunked_list:
                view.print_chunk_tournaments(chunk, i)
                i += 1

        elif len(chunked_list) > 9:
            i = 1
            chunks = ControllerTournament.slice_results(chunked_list)
            for elt in chunks[0]:
                view.print_chunk_tournaments(elt, i)
                i += 1
            j = 1
            while j < len(chunks):
                see_more = view.see_more_results()
                if see_more in "yY":
                    print("\n")
                    for elt in chunks[j]:
                        view.print_chunk_tournaments(elt, i + j - 1)
                        j += 1
                elif see_more in "nN":
                    break

            return len(chunked_list)

    def get_all_tournaments(self):
        view.print_all_tournaments()

        all_tournaments = self.model.tournaments_database.all()

        chunks = ControllerTournament.see_chunks_items(all_tournaments)

        if chunks is None:
            pass

        else:
            see_details_or_not = view.see_details_or_not()

            if see_details_or_not in "yY":

                see_tournament_details = view.see_tournament_details

                tournament_choice = see_tournament_details(all_tournaments)

                searched_tournament = all_tournaments[
                    int(tournament_choice) - 1
                ]

                self.model.deserialize_matches_and_rounds(searched_tournament)

            elif see_details_or_not in "nN":
                pass
