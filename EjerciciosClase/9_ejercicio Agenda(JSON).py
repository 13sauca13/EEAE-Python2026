import json

def cargar_agenda():
    with open(input("Introduzca el nombre de la agenda que quiere cargar: "), "r") as agenda:
        a = json.load(agenda)
    return a

def guardar_agenda(a):
    with open("9_agenda.json", "w") as agenda:
        json.dump(a, agenda, indent=4)

agenda_cargada = cargar_agenda()

guardar_agenda(agenda_cargada)