from .match_models import MatchModel
from .round_models import ModelRound
from datetime import datetime
from operator import attrgetter
from operator import itemgetter
from tinydb import TinyDB
import json


class TournamentModel:
    db = TinyDB("models/tournaments_database.json")
    num_rounds = 0
    rounds_list = []

    def __init__(self, **kwargs):
        TournamentModel.num_rounds += 1
        self.name = kwargs["name"]
        self.location = kwargs["location"]
        self.start_date = kwargs["start_date"]
        self.end_date = kwargs["end_date"]
        self.description = kwargs["description"]
        self.time_control = kwargs["time_control"]
        self.players_list = kwargs["players_list"]
        self.rounds = []

    def __str__(self):
        tournament_info = (
            f"Tournament name: {self.name}\n"
            f"Location: {self.location}\n"
            f"Dates: from {self.start_date} to {self.end_date}\n"
            f"Description: {self.description}\n"
            f"Time control: {self.time_control}\n"
            f"Participants:\n"
        )

        participants_info = "\n".join(
            [
                f"{player[0]} - {player[1]} - ranking: {player[2]}"
                for player in self.players_list
            ]
        )

        rounds_info = "\n".join(
            [
                f"Round {i+1} results: {self.rounds[i]}"
                for i in range(len(self.rounds))
            ]
        )

        return tournament_info + participants_info + "\n\n" + rounds_info

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, new_name):
        if not all(x.isalpha() or x.isspace() for x in new_name):
            print("Please enter a valid name of tournament.")
        self._name = new_name

    @property
    def location(self):
        return self._location.title()

    @location.setter
    def location(self, new_location):
        if all(x.isalpha() or x.isspace() for x in new_location) is False:
            print("Please enter a valid location.")
        self._location = new_location

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_date):
        try:
            new_date = datetime.strptime(
                new_date, "%Y.%m.%d (%H:%M:%S)"
            ).date()
        except ValueError:
            print("Please enter a valid start date (YYYY.MM.DD (HH:MM:SS))")
        self._start_date = new_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_date):
        try:
            new_date = datetime.strptime(
                new_date, "%Y.%m.%d (%H:%M:%S)"
            ).date()
        except ValueError:
            print("Please enter a valid start date (YYYY.MM.DD (HH:MM:SS))")
        self._end_date = new_date

    @property
    def rounds(self):
        return self._rounds

    @rounds.setter
    def rounds(self, new_list):
        if not (isinstance(new_list, list) and len(new_list) == 4):
            print("Please enter a valid list of rounds.")
        self._rounds = new_list

    @property
    def players_list(self):
        return self._players_list

    @players_list.setter
    def players_list(self, new_list):
        if not (isinstance(new_list, list) and len(new_list) == 8):
            print("Please enter a valid list of players.")
        self._players_list = new_list

    @property
    def time_control(self):
        return self._time_control.capitalize()

    @time_control.setter
    def time_control(self, new_time_control):
        if not new_time_control.lower() in ("blitz", "rapid", "bullet"):
            print("Please enter a valid time control (blitz, bullet, rapid).")
        self._time_control = new_time_control

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    def generate_pairs_by_ranking(players):
        rankings_to_sort = sorted(
            players, key=attrgetter("ranking"), reverse=True
        )
        first_half = rankings_to_sort[:4]
        second_half = rankings_to_sort[4:]
        ranking_pairs = [(first_half[i], second_half[i]) for i in range(0, 4)]
        return ranking_pairs

    def invert_pair(pair):
        return (pair[1], pair[0])

    def swiss_pair(list1, n, list2, k, i, j):
        list1[n] = (list2[2 * n], list2[2 * n + i])
        list1[n + k] = (list2[2 * n + 1], list2[2 * n + j])

    def generate_pairs_by_score(self, players, pairs_list):
        rankings_sorted = sorted(
            players, key=attrgetter("ranking"), reverse=True
        )
        scores_to_sort = [(player, player.score) for player in rankings_sorted]
        players_by_score = sorted(
            scores_to_sort, key=itemgetter(1), reverse=True
        )
        players_by_score = [pair[0] for pair in players_by_score]
        score_pairs = [
            (players_by_score[i], players_by_score[i + 1])
            for i in range(0, 7, 2)
        ]
        round_pairs = [players_by_score, score_pairs]
        players_by_score = round_pairs[0]
        round_pairs = round_pairs[1]

        for pair in round_pairs:
            inverted_pair = TournamentModel.invert_pair(pair)
            pair_index = round_pairs.index(pair)
            n = pair_index

            if (pair or inverted_pair) in pairs_list:
                print("Redundant pair: ")
                print(
                    f"{pair[0].last_name} ({pair[0].id_number}) vs {pair[1].last_name} ({pair[1].id_number})\n"
                )

                if n in range(0, 2):
                    TournamentModel.swiss_pair(
                        round_pairs, n, players_by_score, 1, 2, 3
                    )
                    inverted_pair = TournamentModel.invert_pair(round_pairs[n])

                    if (round_pairs[n] or inverted_pair) in pairs_list:
                        print("Redundant pair: ")
                        print(
                            f"{round_pairs[n][0].last_name} ({round_pairs[n][0].id_number})"
                            + f" vs {round_pairs[n][1].last_name} ({round_pairs[n][1].id_number})\n"
                        )
                        TournamentModel.swiss_pair(
                            round_pairs, n, players_by_score, 1, 3, 2
                        )

                        if (round_pairs[n] or inverted_pair) in pairs_list:
                            print("Redundant pair:")
                            print(
                                f"{round_pairs[n][0].last_name} ({round_pairs[n][0].id_number})"
                                + f" vs {round_pairs[n][1].last_name} ({round_pairs[n][1].id_number})\n"
                            )
                            if n in range(0, 2):
                                TournamentModel.swiss_pair(
                                    round_pairs, n, players_by_score, 2, 4, 5
                                )
                                round_pairs[n + 1] = (
                                    players_by_score[2 * n + 2],
                                    players_by_score[2 * n + 3],
                                )
                            elif n == 2:
                                TournamentModel.swiss_pair(
                                    round_pairs,
                                    n,
                                    players_by_score,
                                    -1,
                                    -1,
                                    -2,
                                )
                                round_pairs[n + 1] = (
                                    players_by_score[2 * n + 2],
                                    players_by_score[2 * n + 3],
                                )
                elif n == 3:
                    TournamentModel.swiss_pair(
                        round_pairs, n, players_by_score, -1, -1, -2
                    )
                    inverted_pair = TournamentModel.invert_pair(round_pairs[n])
                    if (round_pairs[n] or inverted_pair) in pairs_list:
                        print(f"Redundant pair: {round_pairs[n]}\n")
                        TournamentModel.swiss_pair(
                            round_pairs, n, players_by_score, -1, -2, -1
                        )
                        if (round_pairs[n] or inverted_pair) in pairs_list:
                            print(f"Redundant pair: {round_pairs[n]}\n")
                            TournamentModel.swiss_pair(
                                round_pairs, n, players_by_score, -2, -3, -4
                            )
                            round_pairs[n - 1] = (
                                players_by_score[4],
                                players_by_score[5],
                            )
        return round_pairs

    def serialize_tournament(self):
        serialized_tournament = {}
        json.dumps(serialized_tournament, default=str)
        serialized_tournament["name"] = self.name
        serialized_tournament["location"] = self.location
        serialized_tournament["start_date"] = self.start_date.strftime(
            "%Y.%m.%d (%H:%M:%S)"
        )
        serialized_tournament["end_date"] = self.end_date.strftime(
            "%Y.%m.%d (%H:%M:%S)"
        )
        serialized_tournament["description"] = self.description
        serialized_tournament["time_control"] = self.time_control
        serialized_tournament["players_list"] = self.players_list
        serialized_tournament["rounds"] = self.rounds
        return serialized_tournament

    def deserialize_tournament(serialized_tournament):
        name = serialized_tournament["name"]
        location = serialized_tournament["location"]
        start_date = serialized_tournament["start_date"]
        end_date = serialized_tournament["end_date"]
        description = serialized_tournament["description"]
        time_control = serialized_tournament["time_control"]
        players_list = serialized_tournament["players_list"]
        rounds = serialized_tournament["rounds"]
        deserialized_tournament = TournamentModel(
            name=name,
            location=location,
            start_date=start_date,
            end_date=end_date,
            description=description,
            time_control=time_control,
            players_list=players_list,
        )
        deserialized_tournament.rounds = rounds
        return deserialized_tournament

    def save_tournament_to_tournaments_database(self):
        TournamentModel.tournaments_database.insert(self)

    def deserialize_matches_and_rounds(tournament):
        ModelRound.number_of_rounds = 0
        tournament_rounds = tournament["rounds"]
        tournament_deserialized_rounds = []

        for round in tournament_rounds:
            round_matches = round["matches"]
            round_deserialized_matches = []
            for match in round_matches:
                deserialized_match = ModelMatch.deserialize_match(match)
                round_deserialized_matches.append(deserialized_match)
            round["matches"] = round_deserialized_matches

            deserialized_round = ModelRound.deserialize_round(round)
            tournament_deserialized_rounds.append(deserialized_round)

        tournament["rounds"] = tournament_deserialized_rounds
        print(f"\n{tournament['name']} of {tournament['location']}\n")

        for round in deserialized_trnmt.rounds:
            print(round)
