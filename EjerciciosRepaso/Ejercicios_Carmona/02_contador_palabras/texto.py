def contar_palabras(texto):
    return len(texto.split())


class Texto:
    def __init__(self, texto):
        self.texto = texto

    def contar_palabras(self):
        return contar_palabras(self.texto)
