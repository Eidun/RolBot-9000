import json


class Reader:
    def __init__(self):
        self.names = {
            'arquetipos': "archives/arquetipos.json",
            'entrenamientos': "archives/entrenamientos.json",
            'flujo_de_creacion': "archives/flujo.json",
            'historial': "archives/historial.json",
            'magia': "archives/magia.json",
            'reglas_generales': "archives/generales.json",
            'ventajas_desventajas': "archives/ventajas-desventajas.json",
            'experiencia': "archives/experiencia.json"
        }

    def get_json(self, name: str, param1):
        if name in self.names:
            if name == "historial" and param1 is int:
                return self.get_historial(name, param1, self.names[name])
            elif name == "arquetipos":
                return self.get_arquetipos(name, self.names[name], param1)
            elif name == "entrenamientos":
                return self.get_entrenamientos(name, self.names[name], param1)
            elif name == "flujo_de_creacion":
                return self.get_creacion(name, self.names[name])
            elif name == "magia":
                return None
            elif name == "reglas_generales":
                return None
            elif name == "ventajas_desventajas":
                return self.get_ven_des(name, self.names[name], param1)
            elif name == "experiencia":
                return self.get_experiencia(name, self.names[name])
            else:
                return "lo sentimos, no hay eso que pides"
        else:
            return "lo sentimos, no hay eso que pides"

    def get_historial(self, name: str, param1: int, root):
        data = self.read_json(root)
        with open(root) as data_file:
            data = json.load(data_file)
            result = ""
            if (param1 == None):
                result = ["", "", ""]
                for i in range(100):
                    if (i <= 33):
                        result[0] += str(data[name]["elemento"][i]["id"]) + "-" + data[name]["elemento"][i][
                            "name"] + "\n"
                    if (i > 33 and i <= 66):
                        result[1] += str(data[name]["elemento"][i]["id"]) + "-" + data[name]["elemento"][i][
                            "name"] + "\n"
                    if (i > 66):
                        result[2] += str(data[name]["elemento"][i]["id"]) + "-" + data[name]["elemento"][i][
                            "name"] + "\n"
            elif (param1 > 0 and param1 < 101):
                result += str(data[name]["elemento"][param1 - 1]["name"]) + "-" + data[name]["elemento"][param1 - 1][
                    "value"] + "\n"
            elif (param1 > 100 or param1 <= 0):
                result += "ese historial no existe"
            return result

    def get_creacion(self, name: str, root: str):
        data = self.read_json(root)
        result = ""
        for i in range(6):
            result += str(data[name]["elemento"][i]["id"]) + "-" + data[name]["elemento"][i]["value"] + "\n"
        return result

    def get_arquetipos(self, name: str, root: str, param1: str):
        data = self.read_json(root)
        result = ""
        if (param1 == None):
            for i in range(6):
                result += str(data[name]["categoria"][i]["name"]) + "\n"
        elif (param1 == "akuma"):
            result += "ANILLOS\n" + str(data[name]["categoria"][0]["anillos"]) + "PUNTOS DISPONIBLES\n" + str(
                data[name]["categoria"][0]["puntos"]) + "TIPOS DE AKUMA\n"
            for j in range(7):
                result += str(data[name]["categoria"][0]["tipos"][j]["name"]) + "-" + str(
                    data[name]["categoria"][0]["tipos"][j]["value"]) + "\n"
            result += "LIMITES\n" + str(data[name]["categoria"][0]["limites"]) + "\n" + "DEBILIDADES\n" + str(
                data[name]["categoria"][0]["debilidades"]) + "\n" + "PODERES\n" + str(
                data[name]["categoria"][0]["poderes"]) + "\n"
        elif (param1 == "esper"):
            result += "ANILLOS\n" + str(data[name]["categoria"][1]["anillos"]) + "PUNTOS DISPONIBLES\n" + str(
                data[name]["categoria"][1]["puntos"]) + "TIPOS DE ESPER\n"
            for j in range(2):
                result += str(data[name]["categoria"][1]["tipos"][j]["name"]) + "-" + str(
                    data[name]["categoria"][1]["tipos"][j]["value"]) + "\n"
            result += "LIMITES\n" + str(data[name]["categoria"][1]["limites"]) + "\n" + "PODERES\n" + str(
                data[name]["categoria"][1]["poderes"]) + "\n"
        elif (param1 == "monje" or param1 == "juramentado"):
            result += "ANILLOS\n" + str(data[name]["categoria"][2]["anillos"]) + "PUNTOS DISPONIBLES\n" + str(
                data[name]["categoria"][2]["puntos"]) + "KAMIS\n"
            for j in range(5):
                result += str(data[name]["categoria"][2]["tipos"][j]["name"]) + "-" + str(
                    data[name]["categoria"][2]["tipos"][j]["value"]) + "\n"
            result += "LIMITES\n" + str(data[name]["categoria"][2]["limites"]) + "\n" + "DEBILIDADES\n" + str(
                data[name]["categoria"][2]["debilidades"]) + "\n" + "PODERES\n" + str(
                data[name]["categoria"][2]["poderes"]) + "\n"
            result += "OFUDAS\n" + str(data[name]["categoria"][2]["ofudas"]) + "\n" + "NOTAS\n" + str(
                data[name]["categoria"][2]["notas"]) + "VOTOS\n"
            for j in range(6):
                result += str(data[name]["categoria"][2]["votos"][j]["voto"]) + "-" + str(
                    data[name]["categoria"][2]["votos"][j]["value"]) + "\n"
        elif (param1 == "shinsengumi" or param1 == "ronin" or param1 == "ikkitousen"):
            result += "ANILLOS\n" + str(data[name]["categoria"][3]["anillos"]) + "PUNTOS DISPONIBLES\n" + str(
                data[name]["categoria"][3]["puntos"]) + "\nCAMINOS\n"
            for j in range(2):
                result += str(data[name]["categoria"][3]["caminos"][j]["name"]) + "-" + str(
                    data[name]["categoria"][3]["caminos"][j]["value"]) + "\n"
            result += "BUSHIDO\n" + str(data[name]["categoria"][3]["bushido"]["name"]) + "-" + str(
                data[name]["categoria"][3]["bushido"]["value"]) + "\nLEGADOS\n"
            result += "SHINSENGUMI\n" + "-" + str(
                data[name]["categoria"][3]["bushido"]["legado"]["shinsengumi"]["dato"]) + "\nESCUELAS\n"
            for k in range(10):
                result += str(
                    data[name]["categoria"][3]["bushido"]["legado"]["shinsengumi"]["caminos"][k]["name"]) + "-" + str(
                    data[name]["categoria"][3]["bushido"]["legado"]["shinsengumi"]["caminos"][k]["value"]) + "\n"
            result += "IKKITOUSEN\n" + "-" + str(
                data[name]["categoria"][3]["bushido"]["legado"]["ikkitousen"]["dato"]) + "\nESCUELAS\n"
            for l in range(5):
                result += str(data[name]["categoria"][3]["bushido"]["legado"]["ikkitousen"]["caminos"][l][
                                  "name"]) + "-" + str(
                    data[name]["categoria"][3]["bushido"]["legado"]["ikkitousen"]["caminos"][l]["value"]) + "\n"
            result += "ZENRYOKU\n" + str(data[name]["categoria"][3]["zenryoku"]["name"]) + "-" + str(
                data[name]["categoria"][3]["zenryoku"]["value"]) + "\n" + str(
                data[name]["categoria"][3]["zenryoku"]["zenryoku"])
            result += "\nRONIN\n" + str(data[name]["categoria"][3]["ronin"]["name"]) + "-" + str(
                data[name]["categoria"][3]["ronin"]["value"]) + "\n" + str(
                data[name]["categoria"][3]["ronin"]["legado"])
            result += "\nLIMITES\n" + str(data[name]["categoria"][3]["limites"]) + "\nPODERES\n" + str(
                data[name]["categoria"][3]["poder"])
        elif (param1 == "consagrado"):
            result += "ANILLOS\n" + str(data[name]["categoria"][4]["anillos"]) + "\nPUNTOS DISPONIBLES\n" + str(
                data[name]["categoria"][4]["puntos"]) + "\nLIMITES\n" + str(data[name]["categoria"][4]["limites"])
        elif (param1 == "espia" or param1 == "contratista" or param1 == "mago"):
            result += "ANILLOS\n" + str(data[name]["categoria"][5]["anillos"]) + "\mESPECIALIZACION\n"
            for i in range(3):
                result += str(data[name]["categoria"][5]["especializacion"][i]["name"]) + "-" + str(
                    data[name]["categoria"][5]["especializacion"][i]["value"]) + "\n"
            result += "TIEMPO EN ACTIVO-" + str(data[name]["categoria"][5]["tiempo"]["dato"]) + "\n"
            for i in range(8):
                result += str(data[name]["categoria"][5]["tiempo"]["tabla"][i]["years"]) + "-" + str(
                    data[name]["categoria"][5]["tiempo"]["tabla"][i]["value"]) + "\n"
            result += "VENTAJAS-" + str(data[name]["categoria"][5]["ventajas"]["dato"]) + "\n"
            for i in range(3):
                result += str(data[name]["categoria"][5]["ventajas"]["ventajas"][i]["name"]) + "-" + str(
                    data[name]["categoria"][5]["ventajas"]["ventajas"][i]["value"]) + "\n"
            result += "LIMITES\n" + str(data[name]["categoria"][5]["limites"])
        else:
            result += "Lo siento, no tenemos arquetipos para gays"
        return result

    def get_experiencia(self, name: str, root: str):
        data = self.read_json(root)
        result = ""
        result += "RECOMPENSAS\n"
        for i in range(5):
            result += data["experiencia"]["recompensas"][i]["cantidad"] + "-" + data["experiencia"]["recompensas"][i][
                "value"] + "\n"
        result += "PUNTOS INICIALES\n" + data["experiencia"]["iniciales"] + "\nCONVERSION DE PUNTOS AKUMA-5A" + \
                  data["experiencia"]["conversion"] + "\nNOTAS\n" + data["experiencia"][
                      "notas"] + "\nCOSTE DE LOS ANILLOS\n" + data["experiencia"][
                      "coste-anillos"] + "\nCOSTE HABILIDAD\n" + data["experiencia"]["coste-habilidad"]
        return result

    def get_ven_des(self, name: str, root: str, param1: str):
        data = self.read_json(root)
        result = ""
        if (param1 == None):
            result += "VENTAJAS\n"
            for i in range(data["ventajas"]["ventajas"].__len__()):
                result += data["ventajas"]["ventajas"][i]["name"] + " " + data["ventajas"]["ventajas"][i][
                    "puntos"] + "\n"
            result += "DESVENTAJA EXTRA\n" + data["ventajas"]["desventaja-extra"]["name"] + "-" + \
                      data["ventajas"]["desventaja-extra"]["value"] + "\n"
            result += "VENTAJAS/DESVENTAJAS NO PERMITIDAS DE 5A\n"
            for i in range(data["ventajas"]["no-permitidas"].__len__()):
                result += data["ventajas"]["no-permitidas"][i]["value"] + "\n"
            return result
        else:
            for i in range(data["ventajas"]["ventajas"].__len__()):
                if (param1 == data["ventajas"]["ventajas"][i]["name"]):
                    return data["ventajas"]["ventajas"][i]["value"]
            return "No existe esa ventaja o ya ha sido mostrada"

    def get_entrenamientos(self, name: str, root: str, param1: str):
        data = self.read_json(root)
        result = ""
        if (param1 == None):
            result += "ENTRENAMIENTOS\n"
            for i in range(data["entrenamientos"].__len__()):
                result += data["entrenamientos"][i]["clan"] + "\n"
            result += data["nota"]
            return result
        else:
            for i in range(data["entrenamientos"].__len__()):
                if (param1 == data["entrenamientos"][i]["clan"]):
                    for j in range(data["entrenamientos"][i]["escuelas"].__len__()):
                        result += str(data["entrenamientos"][i]["escuelas"][j]["escuela"]) + "->" + str(
                            data["entrenamientos"][i]["escuelas"][j]["grupo"]) + "\n"
                    return result
            return "No existe esa ventaja o ya ha sido mostrada"

    def read_json(self, root: str):
        with open(root, 'r', encoding="utf-8") as data_file:
            return json.load(data_file)
