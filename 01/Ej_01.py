"""Ejercicio 1: 
Calculadora básica con clases 
Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números. 
Incluye un constructor que inicialice los dos números como atributos. """

from Clases import Calculadora

while 1:
   
    print("Elige la operación que quieres hacer\n--------------------\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n")
    opcion = input("Introduce la opción: ")

    n1 = Calculadora(float(input("Introduce el primer número: ")))
    n2 = Calculadora(float(input("Introduce el segundo número: ")))

    if opcion == "1":
        print(f"Resultado: {n1.sumar(n2):.2f}")
    elif opcion == "2":
        print(f"Resultado: {n1.restar(n2):.2f}")
    elif opcion == "3":
        print(f"Resultado: {n1.multiplicar(n2):.2f}")
    elif opcion == "4":
        print(f"Resultado: {n1.dividir(n2):.2f}")
    else:
        print("Opción no válida")
    
    print("----------------------------------------------------")