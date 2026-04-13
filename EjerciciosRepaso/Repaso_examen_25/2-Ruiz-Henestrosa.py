
# Ejercicio 2
# Escribe un programa que convierta una cantidad de metros a kilómetros, centímetros y milímetros. 
# La función debe recibir la cantidad de metros como parámetro y devolver un 
# diccionario con las conversiones.
# Contempla validar que la entrada sea un número positivo.

def conver(metros):
    try:
        if metros <=0:
            raise ValueError('Tiene que ser un número positivo')
        else:
            km=round(metros/1000,2)
            cm=round(metros*100,2)
            mil=round(metros*1000,2)
            conversion={
                'Kilómetros':km,
                'Centímetros':cm,
                'Milímetros':mil
                }
        return conversion
    except ValueError as e:
        return e

while True:
    print('\n___CONVER_APP___\n')
    print('Esta APP convierte los metros en Km, cm y mm\n')
    print('Pulsa 1 para comenzar o 0 para salir')
    opcion=int(input('Indica tu opción: '))
    try:
        if opcion < 0 or opcion > 1:
            raise ValueError('\nLa opción indicada no es correcta')
        elif opcion == 0:
            print('\nGacias por usa CONVER_APP.\n')
            break
        else:
            print(conver(int(input('Indica los metros: '))))
    except ValueError as e:
        print(e)


