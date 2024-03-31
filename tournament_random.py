import random
from chesscenter.utils.constants import COUNT_RANDOM_PLAYER
from chesscenter.utils.bases.tournaments import BaseTournament
from chesscenter.models.player_models import PlayerModel
from chesscenter.models.tournament_models import TournamentModel
from chesscenter.models.match_models import MatchModel
from chesscenter.models.round_models import RoundModel
from chesscenter.random_variables.player_random import RandomPlayer
from chesscenter.random_variables.match_random import RandomMatch
from chesscenter.random_variables.round_random import RandomRound

from tinydb import Query
from faker import Faker

fake = Faker()


class RandomTournament(BaseTournament):
    # Database of tournament names
    names = [
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

    # Database of start dates
    start_dates = [
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
    end_dates = [
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
    dates_attributed = []

    time_control = ["Blitz", "Rapid", "Bullet"]

    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = ""
        self.tournament_models = TournamentModel
        self.match_models = MatchModel
        self.round_models = RoundModel
        self.player_model = PlayerModel

    def get_tournament(self):
        name = random.choice(self.name)
        location = fake.city()
        time_control = random.choice(self.time_control)
        description = ""
        start_date = random.choice(self.start_date)
        end_date = random.choice(self.end_date)
        self.dates_attributed.append(start_date)
        return name, location, start_date, end_date, description, time_control

    def generate_tournament(self):
        random_tournament_inputs = self.generate_random_tournament_inputs()

        # Step 2: Adding 8 random players to the tournament
        self.add_random_players_to_tournament()

        # Step 3: Starting a loop of 4 rounds
        self.generate_rounds()

        # Step 8: Ending the tournament and printing the results
        self.end_tournament(random_tournament_inputs)

    def add_random_players_to_tournament(self):
        # Code to add random players to the tournament
        pass

    def generate_rounds(self):
        # Code to generate rounds
        pass

    def end_tournament(self, tournament_inputs):
        # Code to end the tournament and print the results
        pass

    def generate_tournaments(self):
        """A funtion to generate five random tournaments."""

        for i in range(1, 11):

            # Step 1 : Starting a tournament with random details
            # (name, location, start date, end date, description, time control)

            tournament = RandomTournament.get_tournament()

            # Step 2: Adding 8 random players to the tournament
            # Each player has been previously generated randomly
            # with RandomPlayer.generate_random_player() function
            # and added to ModelPlayer.players_database database
            # of all players.
            self.tournament_players.truncate()

            id_numbers = self.db_id_players[: len(self.players_database)]

            tournament_random_id_numbers = random.sample(id_numbers, 8)

            for random_id_number in tournament_random_id_numbers:
                Player = Query()
                results_players_database = (
                    self.player_model.players_database.search(
                        Player.id_number == int(random_id_number)
                    )
                )
                print(results_players_database)
                for result in results_players_database:
                    self.player_model.save_tournament_player(result)

            self.tournament_models.rounds_list = []
            pairs_list = []

            deserialized_players = []

            for player in self.player_model.tournament_players:
                deserialized_player = player.deserialize_player(player)
                deserialized_players.append(deserialized_player)

            # Step 3: Starting a loop of 4 rounds

            deserialized_rounds = []

            for j in range(1, 5):

                # Step 4: Starting a round

                random_round = RandomRound.generate_random_round_inputs(j, i)
                start_date = random_round[0]

                # Step 5: Generating matches
                # according to Swiss-pairing algorithm

                if not self.tournament_models.rounds_list:
                    generate_pairs = (
                        self.tournament_models.generate_pairs_by_ranking
                    )
                    round_pairs = generate_pairs(deserialized_players)
                    pairs_list.extend(round_pairs)

                elif len(self.tournament_models.rounds_list) in range(1, 5):
                    gen_pairs = self.tournament_models.generate_pairs_by_score
                    round_pairs = gen_pairs(
                        self.tournament_models,
                        deserialized_players,
                        pairs_list,
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

                    serialized_match = self.match_models.serialize_match(match)
                    self.round_models.list_of_matches.append(serialized_match)

                    deserialized_match = self.match_models.deserialize_match(
                        serialized_match
                    )
                    deserialized_matches.append(deserialized_match)

                # Step 7 : Ending the round before starting the next one

                end_date = random_round[1]

                rounds = self.round_models(
                    deserialized_matches, start_date, end_date
                )

                deserialized_rounds.append(rounds)

                serialized_round = RandomRound.serialize_random_round(rounds)

                round_serialized_matches = []
                round_deserialized_matches = serialized_round["matches"]
                for match in round_deserialized_matches:
                    serialized_match = self.match_models.serialize_match(match)
                    round_serialized_matches.append(serialized_match)
                serialized_round["matches"] = round_serialized_matches

                self.tournament_models.rounds_list.append(serialized_round)

                self.round_models.list_of_matches = []

            # Step 8 : Ending the tournament and printing the results

            tournament_players_names = []

            for player in player.tournament_players:
                new_ranking = player["ranking"] + player["score"]
                player_name = player["last_name"]
                player_id_number = player["id_number"]
                tournament_players_names.append(
                    (player_name, player_id_number, new_ranking)
                )

            tournament = self.tournament_models(
                tournament[0],
                tournament[1],
                tournament[2],
                tournament[3],
                tournament[4],
                tournament[5],
                tournament_players_names,
            )

            tournament.rounds = self.tournament_models.rounds_list

            serialized_tournament = RandomTournament.self.serialize_tournament(
                tournament
            )

            self.tournament_models.save_tournament_to_tournaments_database(
                serialized_tournament
            )


if __name__ == "__main__":
    for _ in range(COUNT_RANDOM_PLAYER):
        player = RandomPlayer.generate_players()
        serialized_player = PlayerModel.serialize_player(player)
        PlayerModel.save_db_players(serialized_player)

    # Nous générons un tournoi aléatoire avec ces 8 joueurs
    RandomTournament.generate_tournaments()
