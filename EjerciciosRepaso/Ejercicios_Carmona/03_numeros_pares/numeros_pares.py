"""Ejercicio 3:
Lista de numeros pares
Crea una clase Numeros con un atributo que sea una lista de enteros.
Incluye un metodo que devuelva solo los numeros pares de esa lista.
"""

from numeros import Numeros


while True:
    lista_numeros = []

    print("\nIntroduce numeros enteros para obtener los pares.")
    print("Pulsa Enter sin escribir nada para mostrar el resultado.")

    while True:
        entrada = input("Introduce un numero: ")

        if entrada == "":
            break

        lista_numeros.append(int(entrada))

    numeros = Numeros(lista_numeros)
    print(f"Numeros pares: {numeros.pares()}")

    continuar = input("\nPulsa Enter para salir o escribe algo para repetir: ")
    if continuar == "":
        print("Programa finalizado.")
        break
