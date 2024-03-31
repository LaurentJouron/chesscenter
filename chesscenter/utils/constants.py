from datetime import datetime, timedelta

NUMBER_OF_DAY: int = 0
NUMBER_OF_ROUND: int = 4
NUMBER_OF_PLAYERS: int = 8
COUNT_RANDOM_PLAYER: int = 50

DB_PLAYERS: str = "chesscenter/data/db_players.json"
DB_TOURNAMENTS: str = "chesscenter/data/db_tournaments.json"
DB_TOURNAMENTS_PLAYERS: str = "chesscenter/data/tournament_players.json"

SIZE_LINE: int = 90

CONFIRMATION_MENU: dict = {
    "1": "Confirm",
    "2": "Change",
}


# Calcul de la date limite pour être majeur (18 ans)
BIRTHDAY_LIMIT = datetime.now() - timedelta(days=18 * 365)
