from values import MODE
from db_adapter import DBAdapter


class InfoCard:
    def __init__(self, identificador: str):
        self.identificador = identificador
        self.get_card()

    def get_card(self):
        return DBAdapter(MODE).get_cards_db(self.identificador)

