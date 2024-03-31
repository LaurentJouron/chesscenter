import random
from ..models.match_models import MatchModel


class RandomMatch:
    def generate_random_match(self, player2):
        score_options = ["W", "L", "D"]
        result = random.choice(score_options)
        if result == "L":
            winner = player2
            loser = self
            winner_score = 1
            loser_score = 0
        elif result == "W":
            winner = self
            loser = player2
            winner_score = 1
            loser_score = 0
        else:
            winner = None
            loser = None
            winner_score = 0.5
            loser_score = 0.5

        if winner:
            winner.score += winner_score
        if loser:
            loser.score += loser_score

        return MatchModel(
            winner.last_name if winner else "",
            winner_score,
            loser.last_name if loser else "",
            loser_score,
        )
