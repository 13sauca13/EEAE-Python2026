"""
Ejercicio 2
Escribe un programa que convierta una cantidad de metros a kilómetros, centímetros y milímetros. 
La función debe recibir la cantidad de metros como parámetro y devolver un diccionario con las conversiones.

Contempla validar que la entrada sea un número positivo.
"""
def conversion(m):
    dicc = {}
    dicc["Kilometros"] = m / 1000
    dicc["centimetros"] = m * 100
    dicc["milimetros"] = m / 0.001 
    return dicc

while 1:
    try:
        metros = float(input("Introduce un valor en metros: "))
        if metros <= 0:
            print("Introduzca un valor por encima de 0: ")
        else:
            diccResultado = conversion(metros)
            print(f"{metros:.2f}m equivalen a:\n{diccResultado['Kilometros']:.2f}Km\n{diccResultado['centimetros']:.2f}cm\n{diccResultado['milimetros']:.2f}mm.  ")


    except ValueError:
        print("El dato introducido no es un número valido.")