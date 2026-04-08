class Numeros:
    def __init__(self, lista):
        self.lista = lista

    def pares(self):
        lista_pares = []

        for numero in self.lista:
            if numero % 2 == 0:
                lista_pares.append(numero)

        return lista_pares
