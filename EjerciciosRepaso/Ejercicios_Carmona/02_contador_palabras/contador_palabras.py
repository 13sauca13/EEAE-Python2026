"""Ejercicio 2:
Contador de palabras
Escribe una funcion que reciba una cadena de texto y devuelva cuantas palabras contiene.
Luego, crea una clase Texto que use esa funcion como metodo y almacene el texto como atributo.
"""

from texto import Texto


while True:
    frase = input("\nIntroduce una frase para contar las palabras o pulsa Enter para salir:\n")
    if frase == "":
        print("Programa finalizado.")
        break

    texto = Texto(frase)
    print(f"Numero de palabras: {texto.contar_palabras()}")
