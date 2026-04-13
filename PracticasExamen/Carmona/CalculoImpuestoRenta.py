"""
Ejercicio 1
Crea una aplicación que calcule el impuesto sobre la renta de una persona. 
La aplicación debe pedir al usuario su ingreso anual, 
y calcular el impuesto basado en las siguientes tasas:

Hasta 10000€: 10%
De 10001€ a 20000€: 15%
De 20001€ a 30000€: 20%
Más de 30000€: 25%
La aplicación puede manejar excepciones para validar la entrada del usuario.

Debe mostrar el impuesto total a pagar.
"""
def calcularImpuesto(ia):
    if ia <= 10000:
        return 0.10
    elif ia <= 20000:
        return 0.15
    elif ia <= 30000:
        return 0.20
    else:
        return 0.25

while 1:
    try:
        ingresoAnual = float(input("Introduce tu salario anual: "))
        impuestoPorcentaje = calcularImpuesto(ingresoAnual)
        impuestoEuros = (ingresoAnual*impuestoPorcentaje) 
        print(f"Para unos ingresos anuales de {ingresoAnual:.2f}€ el impuesto total a pagar es de: {impuestoEuros:.2f}€.\n")
    
    except ValueError:
        print("Introduce el importe en numero entero o decimal.\n")