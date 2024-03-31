from datetime import datetime
from operator import attrgetter
from operator import itemgetter
from tinydb import TinyDB

from ..utils.constants import DB_TOURNAMENTS
from .match_models import MatchModel
from .round_models import RoundModel


class TournamentModel:
    db = TinyDB(DB_TOURNAMENTS, indent=4)
    db_tournament = db.table("tournament")

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
        participants = "\n".join(
            f"{player[0]} - {player[1]} - rank: {player[2]}"
            for player in self.players_list
        )

        rounds = "\n".join(
            f"Round {round + 1} results: {result}"
            for round, result in enumerate(self.rounds)
        )

        return (
            f"Tournament name: {self.name}\n"
            f"Location: {self.location}\n"
            f"Dates: from {self.start_date} to {self.end_date}\n"
            f"Description: {self.description}\n"
            f"Time control: {self.time_control}\n"
            f"Participants:\n{participants}\n\n"
            f"{rounds}"
        )

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, new_name):
        if not all(char.isalpha() or char.isspace() for char in new_name):
            print("Please enter a valid name of tournament.")
        self._name = new_name

    @property
    def location(self):
        return self._location.title()

    @location.setter
    def location(self, new_location):
        if not all(char.isalpha() or char.isspace() for char in new_location):
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
    def time_control(self, time_control):
        if time_control.lower() not in ("blitz", "rapid", "bullet"):
            print("Please enter a valid time control (blitz, bullet, rapid).")
        self._time_control = time_control

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    def generate_pairs_by_rank(self):
        rank_to_sort = sorted(self, key=attrgetter("rank"), reverse=True)
        first_half = rank_to_sort[:4]
        second_half = rank_to_sort[4:]
        return [(first_half[i], second_half[i]) for i in range(4)]

    def invert_pair(self):
        return self[1], self[0]

    def swiss_pair(self, n, list2, k, i, j):
        self[n] = (list2[2 * n], list2[2 * n + i])
        self[n + k] = (list2[2 * n + 1], list2[2 * n + j])

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
                            f"{round_pairs[n][0].last_name} ({round_pairs[n][0].id_number}) "
                            f"vs {round_pairs[n][1].last_name} ({round_pairs[n][1].id_number})\n"
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

    def save_tournament_to_tournaments_database(self):
        TournamentModel.db_tournament.insert(self)

    def deserialize_matches_and_rounds(self):
        ModelRound.number_of_rounds = 0
        tournament_rounds = self["rounds"]

        tournament_deserialized_rounds = []

        # For each round of the tournament
        for round in tournament_rounds:
            round_matches = round["matches"]

            # All embedded matches are deserialized
            round_deserialized_matches = []
            for match in round_matches:
                deserialized_match = MatchModel.deserialize_match(match)
                round_deserialized_matches.append(deserialized_match)
            round["matches"] = round_deserialized_matches

            # Then the round is deserialized
            deserialized_round = RoundModel.deserialize_round(round)

            # Then added to the tournament to be deserialized
            tournament_deserialized_rounds.append(deserialized_round)

            # Then all deserialized rounds are added to the tournament
        self["rounds"] = tournament_deserialized_rounds
        print(f"\n{self['name']} of {self['location']}\n")

        # Finally, the tournament is deserialized
        deserialized_trnmt = TournamentModel.deserialize_tournament(self)
        line = 100 * "-"
        print(line)
        print(f"\nTournament name: {deserialized_trnmt.name}")
        print(f"\nLocation: {deserialized_trnmt.location}")
        print(f"\nDescription: {deserialized_trnmt.description}")
        print(f"\nTime Control: {deserialized_trnmt.time_control}")
        print("\nParticipants:\n")
        dt_players_list = deserialized_trnmt.players_list
        for i in range(8):
            print(
                f"({dt_players_list[i][1]}) "
                f"{dt_players_list[i][0]} "
                f"- rank: {dt_players_list[i][2]} "
            )
        print("\nResults\n")
        for round in deserialized_trnmt.rounds:
            print(round)
        print(line)
