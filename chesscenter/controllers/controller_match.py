from chesscenter.models.model_match import ModelMatch
from chesscenter.views.view_match import ViewMatch


class ControllerMatch:
    """A Controller for Match Class.

    The controller can perform the following actions :

    - Start a match ;
    - Print the winner and the score of a match."""

    def __init__(self, model, view):
        self.model = ModelMatch
        self.view = ViewMatch

    def start_match(first_player, second_player):
        """A function to start a match."""

        first_player_name = first_player.last_name
        first_id = first_player.id_number
        second_player_name = second_player.last_name
        second_id = second_player.id_number
        return ViewMatch.start_match(
            (first_player_name, first_id), (second_player_name, second_id)
        )

    def print_winner_and_score(first_player, second_player):
        """A function to print the winner and the score of a match."""

        match = ModelMatch("", "", "", "")

        first_id = first_player.id_number
        second_id = second_player.id_number

        result = ViewMatch.get_match_result(
            first_player.last_name, first_player.id_number
        )

        if result in "wW":
            result = ModelMatch.first_player_wins(match)
            first_player.score += 1
            match = ModelMatch(
                first_player.last_name, 1, second_player.last_name, 0
            )
            ViewMatch.print_first_player_wins_and_score(
                first_player.last_name,
                first_id,
                second_player.last_name,
                second_id,
            )
            return match

        elif result in "lL":
            result = ModelMatch.second_player_wins(match)
            second_player.score += 1
            match = ModelMatch(
                first_player.last_name, 0, second_player.last_name, 1
            )
            ViewMatch.print_first_player_wins_and_score(
                second_player.last_name,
                second_id,
                first_player.last_name,
                first_id,
            )
            return match

        elif result in "dD":
            result = ModelMatch.draw(match)
            first_player.score += 0.5
            second_player.score += 0.5
            match = ModelMatch(
                first_player.last_name, 0.5, second_player.last_name, 0.5
            )
            ViewMatch.print_draw(
                first_player.last_name,
                first_id,
                second_player.last_name,
                second_id,
            )
            return match
