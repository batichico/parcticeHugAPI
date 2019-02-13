import json

def getData():
    file_path = "jsons/topics.json"
    with open(file_path, "r") as jsonFile:
        data = json.load(jsonFile)
    return data

def get_botones(id_padre):
    data = getData()
    botones = [y for x, y in data.items() if y['padre'] == id_padre]
    botones.append({'padre': id_padre, 'nombre': 'Volver'})
    return(botones)
