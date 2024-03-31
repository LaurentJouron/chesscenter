from models.model_round import ModelRound
from views.view_round import RoundView
from datetime import datetime

view = RoundView()


class ControllerRound:

    def __init__(self):
        self.model = ModelRound

    def start_round(i):
        view.start_round(i)
        start_date = datetime.now().replace(microsecond=0)
        return start_date

    def end_round():
        end_date = datetime.now().replace(microsecond=0)
        return end_date

    def print_round_results(i, start_date, end_date, list_of_matches):
        return view.print_round_results(
            i, start_date, end_date, list_of_matches
        )
