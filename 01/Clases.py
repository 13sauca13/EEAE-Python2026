class Calculadora:
    def __init__(self, numero):
        self.numero = numero
    
    def sumar(self, otro):
        return self.numero + otro.numero
        
    def restar(self, otro):
        return self.numero - otro.numero
        
    def multiplicar(self, otro):
        return self.numero * otro.numero
        
    def dividir(self, otro):
        try:
            return self.numero / otro.numero
        except ZeroDivisionError:
            return "Error: División por cero"
        
