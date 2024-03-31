import json
from chesscenter.models.tournament_models import TournamentModel


class BaseTournament:
    def serialize_tournament(self):
        return json.dumps(
            {
                "name": self.name,
                "location": self.location,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "description": self.description,
                "time_control": self.time_control,
                "players_list": self.players_list,
                "rounds": self.rounds,
            },
            default=str,
        )

    def deserialize_tournament(self):
        name = self["name"]
        location = self["location"]
        start_date = self["start_date"]
        end_date = self["end_date"]
        description = self["description"]
        time_control = self["time_control"]
        players_list = self["players_list"]
        rounds = self["rounds"]
        deserialized_tournament = TournamentModel(
            name=name,
            location=location,
            start_date=start_date,
            end_date=end_date,
            description=description,
            time_control=time_control,
            players_list=players_list,
        )
        deserialized_tournament.rounds = rounds
        return deserialized_tournament
