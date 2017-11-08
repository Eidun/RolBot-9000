from db_adapter import DBAdapter
from values import MODE


class Agent:
    def __init__(self, name: str):
        data = DBAdapter(MODE).get_agent(name)
        self.name = data[0]
        self.amount = data[1]

    def get_card(self):
        return DBAdapter(MODE).get_cards_db(self.name)
