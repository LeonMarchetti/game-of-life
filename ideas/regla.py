# from celula import Celula

class Regla:
    def __init__(self, estado, funcion):
        self.estado = estado
        self.funcion = funcion

    def aplicar(self):
        return self.funcion()
