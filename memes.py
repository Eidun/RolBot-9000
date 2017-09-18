class Memes:

    def __init__(self):
        self.names = {
            'meto_maldad': "aqui_meto_maldad.png",
            'mafioso':  "vs_Zothe_mafioso.png",
            'malvado':  "malvado_feliz.png"
        }

    def get_meme(self, name: str):

        if name in self.names:
            return "memes/"+ self.names[name]
        else:
            return "memes/well_okay.png"
