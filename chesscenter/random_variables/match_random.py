import random
from ..models.match_models import MatchModel


class RandomMatch:

    def generate_random_match(self, player2):
        match = MatchModel("", "", "", "")

        score_options = ["W", "L", "D"]

        result = random.choice(score_options)

        if result == "W":
            result = MatchModel.first_player_wins(match)
            self.score += 1
            match = MatchModel(self.last_name, 1, player2.last_name, 0)
            return match

        elif result == "L":
            result = MatchModel.second_player_wins(match)
            player2.score += 1
            match = MatchModel(self.last_name, 0, player2.last_name, 1)
            return match

        elif result == "D":
            result = MatchModel.draw(match)
            self.score += 0.5
            player2.score += 0.5
            match = MatchModel(self.last_name, 0.5, player2.last_name, 0.5)
            return match
