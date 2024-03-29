import random
import json

from ..models.player_models import PlayerModel
from ..models.tournament_models import TournamentModel
from ..models.match_models import MatchModel
from ..models.round_models import RoundModel
from ..data.db_id_players import players_id
from .player_random import RandomPlayer
from .match_random import RandomMatch
from .round_random import RandomRound

from tinydb import Query


class RandomTournament:
    # Database of tournament names
    tournament_names = [
        "Grand Tournoi",
        "Grand Prix",
        "Chess international",
        "Grand Chess Tour",
        "Grand Prix",
        "Champ",
        "Classic",
        "Cup",
        "Chess Olympiads",
        "WCF Tournoi",
        "Champions tournament",
        "Chess cup",
        "Chess Tour",
        "Grand Tour",
        "Chess Masters",
        "Chess Academy Tournament",
        "Chess Grand Tour",
        "WCF Grand Prix",
        "WCF Grand Tour",
        "Chess Games",
        "WCF Games",
    ]

    # Database of tournament locations
    tournament_locations = [
        "Riga",
        "Helsinki",
        "Paris",
        "Bilbao",
        "Prague",
        "Moscow",
        "Kigali",
        "Johannesburg",
        "Montreal",
        "Sofia",
        "Dakar",
        "Abidjan",
        "Brasilia",
        "Madrid",
        "Denver",
        "Tokyo",
        "Roma",
        "Mexico",
        "Washington",
        "Pristina",
        "Santiago",
        "Bogota",
        "Medellin",
        "London",
        "Malibu",
        "Chicago",
        "Nairobi",
        "Oslo",
        "Gaborone",
        "Dubai",
        "Tehran",
        "Milano",
        "Riyad",
        "Mascate",
        "Tbilisi",
        "Dushanbe",
        "Tunis",
        " Cape Town",
        "Sao Paulo",
        "Rio de Janeiro",
        "Saint Louis",
        "New York",
    ]

    # Database of start dates
    random_start_dates = [
        "2024.03.03 (08:00:00)",
        "2024.03.15 (08:00:00)",
        "2024.05.20 (08:00:00)",
        "2024.06.29 (08:00:00)",
        "2024.07.01 (08:00:00)",
        "2024.07.10 (08:00:00)",
        "2024.08.29 (08:00:00)",
        "2024.09.07 (08:00:00)",
        "2024.09.13 (08:00:00)",
        "2024.10.03 (08:00:00)",
    ]

    # Database of end dates
    random_end_dates = [
        "2024.03.03 (19:00:00)",
        "2024.03.15 (19:00:00)",
        "2024.05.20 (19:00:00)",
        "2024.06.29 (19:00:00)",
        "2024.07.01 (19:00:00)",
        "2024.07.10 (19:00:00)",
        "2024.08.29 (19:00:00)",
        "2024.09.07 (19:00:00)",
        "2024.09.13 (19:00:00)",
        "2024.10.03 (19:00:00)",
    ]

    # List of the random start dates already attributed
    random_dates_attributed = []

    # List of the ID numbers already attributed
    time_control_options = ["Blitz", "Rapid", "Bullet"]

    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = ""

    def generate_random_tournament_inputs():
        random_name = random.choice(RandomTournament.tournament_names)
        random_location = random.choice(RandomTournament.tournament_locations)
        time_control = RandomTournament.time_control_options
        random_time_control = random.choice(time_control)
        description = ""

        j = len(RandomTournament.random_dates_attributed)

        random_start_date = RandomTournament.random_start_dates[j]
        random_end_date = RandomTournament.random_end_dates[j]
        RandomTournament.random_dates_attributed.append(random_start_date)

        return (
            random_name,
            random_location,
            random_start_date,
            random_end_date,
            description,
            random_time_control,
        )

    def serialize_random_tournament(self):
        serialized_tournament = {}
        json.dumps(serialized_tournament, default=str)
        serialized_tournament["name"] = self.name
        serialized_tournament["location"] = self.location
        serialized_tournament["start_date"] = self.start_date
        serialized_tournament["end_date"] = self.end_date
        serialized_tournament["description"] = self.description
        serialized_tournament["time_control"] = self.time_control
        serialized_tournament["players_list"] = self.players_list
        serialized_tournament["rounds"] = self.rounds
        return serialized_tournament

    def generate_ten_random_tournaments():
        """A funtion to generate five random tournaments."""

        for i in range(1, 11):

            # Step 1 : Starting a tournament with random details
            # (name, location, start date, end date, description, time control)

            random_tournament_inputs = (
                RandomTournament.generate_random_tournament_inputs()
            )

            # Step 2: Adding 8 random players to the tournament
            # Each player has been previously generated randomly
            # with RandomPlayer.generate_random_player() function
            # and added to ModelPlayer.players_database database
            # of all players.

            PlayerModel.tournament_players.truncate()

            random_id_numbers = players_id[: len(PlayerModel.players_database)]

            tournament_random_id_numbers = random.sample(random_id_numbers, 8)

            for random_id_number in tournament_random_id_numbers:
                Player = Query()
                results_players_database = PlayerModel.players_database.search(
                    Player.id_number == int(random_id_number)
                )
                print(results_players_database)
                for result in results_players_database:
                    PlayerModel.save_tournament_player(result)

            TournamentModel.rounds_list = []
            pairs_list = []

            deserialized_players = []

            for player in PlayerModel.tournament_players:
                deserialized_player = PlayerModel.deserialize_player(player)
                deserialized_players.append(deserialized_player)

            # Step 3: Starting a loop of 4 rounds

            deserialized_rounds = []

            for j in range(1, 5):

                # Step 4: Starting a round

                random_round = RandomRound.generate_random_round_inputs(j, i)
                start_date = random_round[0]

                # Step 5: Generating matches
                # according to Swiss-pairing algorithm

                if not TournamentModel.rounds_list:
                    generate_pairs = TournamentModel.generate_pairs_by_ranking
                    round_pairs = generate_pairs(deserialized_players)
                    pairs_list.extend(round_pairs)

                elif len(TournamentModel.rounds_list) in range(1, 5):
                    gen_pairs = TournamentModel.generate_pairs_by_score
                    round_pairs = gen_pairs(
                        TournamentModel, deserialized_players, pairs_list
                    )
                    pairs_list.extend(round_pairs)

                # Step 6 : Playing the matches of the round

                deserialized_matches = []

                for k in range(4):

                    first_player = round_pairs[k][0]
                    second_player = round_pairs[k][1]

                    match = RandomMatch.generate_random_match(
                        first_player, second_player
                    )

                    serialized_match = MatchModel.serialize_match(match)
                    RoundModel.list_of_matches.append(serialized_match)

                    deserialized_match = MatchModel.deserialize_match(
                        serialized_match
                    )
                    deserialized_matches.append(deserialized_match)

                # Step 7 : Ending the round before starting the next one

                end_date = random_round[1]

                round = RoundModel(deserialized_matches, start_date, end_date)

                deserialized_rounds.append(round)

                serialized_round = RandomRound.serialize_random_round(round)

                round_serialized_matches = []
                round_deserialized_matches = serialized_round["matches"]
                for match in round_deserialized_matches:
                    serialized_match = MatchModel.serialize_match(match)
                    round_serialized_matches.append(serialized_match)
                serialized_round["matches"] = round_serialized_matches

                TournamentModel.rounds_list.append(serialized_round)

                RoundModel.list_of_matches = []

            # Step 8 : Ending the tournament and printing the results

            tournament_players_names = []

            for player in PlayerModel.tournament_players:
                new_ranking = player["ranking"] + player["score"]
                player_name = player["last_name"]
                player_id_number = player["id_number"]
                tournament_players_names.append(
                    (player_name, player_id_number, new_ranking)
                )

            tournament = TournamentModel(
                random_tournament_inputs[0],
                random_tournament_inputs[1],
                random_tournament_inputs[2],
                random_tournament_inputs[3],
                random_tournament_inputs[4],
                random_tournament_inputs[5],
                tournament_players_names,
            )

            tournament.rounds = TournamentModel.rounds_list

            serialized_tournament = (
                RandomTournament.serialize_random_tournament(tournament)
            )

            TournamentModel.save_tournament_to_tournaments_database(
                serialized_tournament
            )


if __name__ == "__main__":

    # We generate 8 random players

    for _ in range(1, 51):
        player = RandomPlayer.generate_random_player()
        serialized_player = PlayerModel.serialize_player(player)
        PlayerModel.save_player_to_database(serialized_player)

    # We generate a random tournament with these 8 players

    RandomTournament.generate_ten_random_tournaments()
