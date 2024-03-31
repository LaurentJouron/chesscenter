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

    @staticmethod
    def get_tournament():
        name = random.choice(RandomTournament.names)
        location = fake.city()
        time_control = random.choice(RandomTournament.time_control)
        start_date = random.choice(RandomTournament.start_dates)
        end_date = random.choice(RandomTournament.end_dates)
        RandomTournament.dates_attributed.append(start_date)
        return name, location, start_date, end_date, "", time_control

    @staticmethod
    def serialize_tournament(tournament):
        return {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "description": tournament.description,
            "time_control": tournament.time_control,
            "players_list": tournament.players_list,
            "rounds": tournament.rounds,
        }

    @staticmethod
    def generate_tournaments():
        for _ in range(1, 51):
            player = RandomPlayer.generate_players()
            serialized_player = PlayerModel.serialize_player(player)
            player_instance = PlayerModel(**serialized_player)
            PlayerModel.save_player(player_instance)

        for _ in range(10):
            RandomTournament().generate_random_tournament()

    def generate_random_tournament(self):
        tournament_inputs = self.generate_random_tournament_inputs()
        self.add_random_players_to_tournament()
        self.generate_rounds()
        self.end_tournament(tournament_inputs)

    def add_random_players_to_tournament(self):
        PlayerModel.tournament_players.truncate()

        tournament_random_id_numbers = random.sample(50, 8)

        for random_id_number in tournament_random_id_numbers:
            results_players_database = PlayerModel.players_database.search(
                PlayerModel.id_number == int(random_id_number)
            )
            for result in results_players_database:
                PlayerModel.save_tournament_player(result)

    def generate_rounds(self):
        # Code to generate rounds
        pass

    def end_tournament(self, tournament_inputs):
        # Code to end the tournament and print the results
        pass


if __name__ == "__main__":
    RandomTournament.get_tournament()
