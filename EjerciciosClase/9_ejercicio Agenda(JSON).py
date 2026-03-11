import json

with open("EjerciciosClase/9_agenda.json", "r") as agenda:
    a = json.load(agenda)

print(a)