"""Ejercicio 1:
Calculadora basica con clases
Crea una clase Calculadora que tenga metodos para sumar, restar, multiplicar y dividir dos numeros.
Incluye un constructor que inicialice los dos numeros como atributos.
"""

from calculadora import Calculadora


while True:
    print("\nElige la operacion que quieres hacer")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("Pulsa Enter para salir")

    opcion = input("Introduce la opcion: ")

    if opcion == "":
        print("Programa finalizado.")
        break

    numero1 = float(input("Introduce el primer numero: "))
    numero2 = float(input("Introduce el segundo numero: "))

    calculadora = Calculadora(numero1, numero2)

    if opcion == "1":
        print(f"Resultado: {calculadora.sumar():.2f}")
    elif opcion == "2":
        print(f"Resultado: {calculadora.restar():.2f}")
    elif opcion == "3":
        print(f"Resultado: {calculadora.multiplicar():.2f}")
    elif opcion == "4":
        resultado = calculadora.dividir()

        if type(resultado) == str:
            print(resultado)
        else:
            print(f"Resultado: {resultado:.2f}")
    else:
        print("Opcion no valida.")
