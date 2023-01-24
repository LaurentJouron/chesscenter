"""Information for the organisation of chess tournaments."""


class MatchModel:
    """Generates tournament elements."""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
