
# Ejercicio 1
# Crea una aplicación que calcule el impuesto sobre la renta de una persona. La aplicación debe pedir al usuario su ingreso anual y calcular el impuesto basado en las siguientes tasas:
# Hasta 10,000€: 10%
# De 10,001€ a 20,000€: 15%
# De 20,001€ a 30,000€: 20%
# Más de 30,000€: 25%
# La aplicación puede manejar excepciones para validar la entrada del usuario.
# Debe mostrar el impuesto total a pagar.

while True:
    print ('\n____MENU____\n')
    print ('Pulse 1 para iniciar el cálculo')
    print ('Pulse 0 para salir')
    opcion = int(input('Indique su opción: '))
    try:
        if opcion < 0 or opcion > 1:
            raise ValueError('La opción indicada no es correcta')
        elif opcion == 1:
            try:
                nombre= input('Indique su nombre o seudónimo: ')
                sueldo= int(input('Indique su ingreso anual: '))
                if sueldo < 0:
                    raise ValueError('\nNo puedes tener ingresos negativos, si eres autónomo, cierra el chiringuito.')
                elif sueldo == 0:
                    raise ValueError('\nReplantea el negocio, no va muy bien la cosa.')
                elif sueldo <= 10000:
                    sueldo*=0.1
                    print(f'\n{nombre} tienes que pagar {round(sueldo,1)}€, no te quejes que eres de los que menos aporta.')
                elif sueldo > 10000 and sueldo <= 20000:
                    sueldo*=0.15
                    print(f'\n{nombre} tienes que pagar {round(sueldo,1)}€, estás en la parte BAJA de la media de los contribuyentes.')
                elif sueldo > 20000 and sueldo <= 30000:
                    sueldo*=0.2
                    print(f'\n{nombre} tienes que pagar {round(sueldo,1)}€, estás en la parte ALTA de la media de los contribuyentes.')
                elif sueldo > 30000:
                    sueldo*=0.25
                    print(f'\n{nombre} tienes que pagar {round(sueldo,1)}€, debes estar orgulloso, tu aportación paga mi sueldo.')
            except ValueError as e:
                print(e)
        elif opcion == 0:
            print('\n-- Gracias por usar APLI_CALC --\n')
            break
    except ValueError as i:
        print(i)

