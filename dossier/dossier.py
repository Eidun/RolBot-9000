class Dossier:

    def __init__(self):
        self.__repo = "http://akuma.host56.com/dossier/"
        self.names = {
            'agencia': self.__repo + "Agencia_1.png \n" + self.__repo + "Agencia_2.png",
            'd13': self.__repo + "D13_1.png \n" + self.__repo + "D13_2.png",
            'oversight': self.__repo + "Oversight.png",
            'zechs_gebet': self.__repo + "MERC-6Gebet.png",
            'deadcell': self.__repo + "MERC-Dead%20Cell.png",
            'ektors': self.__repo + "MERC-Ektors.png",
            'ordo': self.__repo + "Ordo.png",
            'utopia': self.__repo + "Utopia.png",
            'otros': self.__repo + "Otros.png \n" + self.__repo + "Otros_2.png"
        }

    def get_dossier(self, name: str):

        if name in self.names:
            return self.names[name]
        else:
            return "¿Pero qué mierdas dices?"
