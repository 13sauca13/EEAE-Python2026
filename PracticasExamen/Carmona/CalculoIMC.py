"""
Ejercicio 3
Crea una aplicación que calcule el Índice de Masa Corporal (IMC) de una persona.

La aplicación debe pedir al usuario su peso en kilogramos y su altura en metros,
 y luego calcular el IMC usando la fórmula:  IMC=PESO/ALTURA2
 

Debe mostrar el IMC con dos decimales.
"""
def Calcular(p,a):
    return p/(a**2)

while 1:
    try:
        peso = float(input("Introduce tu peso en Kgs: "))
        altura = float(input("Introduce tu estatura en Metros: "))

        imc = Calcular(peso, altura)

        print(f"Para un peso de {peso:.2f}Kgs y una estatura de {altura:.2f} metros.\nSu IMC es {imc:.2f}.\n")
    
    except ValueError:
        print("Introduce un número entero o con decimales.")