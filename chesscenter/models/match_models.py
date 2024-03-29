import os
import sys
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)


class MatchModel:
    def __init__(self, **kwargs):
        self.player1: str = kwargs["player1"]
        self._score1: float = kwargs["score1"]
        self.player2: str = kwargs["player2"]
        self._score2: float = kwargs["score2"]

    def __repr__(self):
        return f"[({self.player1}, {self.score1}), ({self.player2}, {self.score2})]"

    def __str__(self):  # sourcery skip: remove-unreachable-code
        return f"[({self.player1}, {self.score1}), ({self.player2}, {self.score2})]"

    @property
    def first_score(self):
        return self._score1

    @first_score.setter
    def first_score(self, new_score):
        if new_score not in [0, 0.5, 1]:
            print("Please enter a valid score (0 - 0.5 - 1).")
        self._score1 = new_score

    @property
    def second_score(self):
        return self._score2

    @second_score.setter
    def second_score(self, new_score):
        if new_score not in [0, 0.5, 1]:
            print("Please enter a valid score (0 - 0.5 - 1).")
        self._score2 = new_score

    def first_player_wins(self):
        self._score1 = 1
        self._score2 = 0

    def second_player_wins(self):
        self._score1 = 0
        self._score2 = 1

    def draw(self):
        self._score1 = 0.5
        self._score2 = 0.5

    def serialize_match(self):
        serialized_match = {}
        json.dumps(serialized_match, default=str)
        serialized_match["player1"] = self.player1
        serialized_match["score1"] = self.score1
        serialized_match["player2"] = self.player2
        serialized_match["score2"] = self.score2
        return serialized_match

    def deserialize_match(self):
        player1 = self["player1"]
        score1 = self["score1"]
        player2 = self["player2"]
        score2 = self["score2"]
        return MatchModel(
            player1=player1,
            score1=score1,
            player2=player2,
            score2=score2,
        )
