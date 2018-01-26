import json as json

class Memes:
    def __init__(self):
        self.names = {}
        self.load_obj()

    def get_meme(self, name: str):

        if name in self.names:
            return self.names[name]
        else:
            return "no tenemos ese meme en nuestra base, añadalo"

    def get_list(self):
        message = ""
        for name in self.names:
            message+= name + "\n"
        return message

    def add_meme(self, name: str, link : str):
        print(name + " " + link)
        if name in self.names:
            return "no se ha podido añadir el meme porque ya existía"
        else:
            self.names[name] = link
            self.save_obj()
            return "se ha añadido el meme satisfactoriamente"

    def delete_meme(self, name: str):

        if name in self.names:
            self.names.pop(name)
            self.save_obj()
            return "el objeto ha sido eliminado satisfactoriamente"
        else:
            return "no existe el meme en la base de datos"

    def save_obj(self):
        json_data = json.dumps(self.names)
        f = open("archives/memes/memes.json", "w")
        f.write(json_data)
        f.close()

    def load_obj(self):
        js = open("archives/memes/memes.json")
        self.names = json.load(js)