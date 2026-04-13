
# Ejercicio 3
# Crea una aplicación que calcule el Índice de Masa Corporal (IMC) de una persona.
# La aplicación debe pedir al usuario su peso en kilogramos y su altura en metros, y luego calcular el IMC usando la fórmula:  IMC=PESO/ALTURA2
# Debe mostrar el IMC con dos decimales.

while True:
    print('\n___IMC_APP___\n')
    print('Esta APP devuelve tu IMC\n')
    print('Pulsa 1 para comenzar')
    print('Pulsa 0 para salir de la aplicación')
    opcion=int(input('Indica tu opción: '))
    try:
        if opcion < 0 or opcion > 1:
            raise ValueError('\nLa opción indicada no es correcta')
        elif opcion == 0:
            print('\nGacias por usa IMC_APP.\n')
            break
        elif opcion == 1:
            try:
                peso= float(input('Indica tu peso en KG.: '))
                altura= float(input('Indica tu altura en metros: '))
                if peso < 0 or peso > 300:
                    raise ValueError('\nEl peso indicado no es correcto.')
                elif altura < 0 or altura > 3:
                    raise ValueError('\nLa altura indicada no es correcta.')
                else:
                    print(f'\nSu ICM es {round(peso/altura**2,2)}.')
            except ValueError as e:
                print(e)
    except ValueError as i:
        print(i)

   
