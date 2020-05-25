from random import getrandbits

from colores import Colores


class Celula:
    MUERTO = 0
    VIVO = 1

    def __init__(self, estado_inicial=None):
        if estado_inicial:
            self.estado = estado_inicial
        else:
            self.estado = getrandbits(1)
        self.generacion = 0

    def avanzar(self, vecinos_vivos):
        if self.estado == Celula.MUERTO:
            if vecinos_vivos == 3:
                self.estado = Celula.VIVO
                self.generacion = 0
        elif self.estado == Celula.VIVO:
            if 2 <= vecinos_vivos <= 3:
                self.generacion += 1
            else:
                self.estado = Celula.MUERTO

    def dibujar(self):
        if self.estado == Celula.MUERTO:
            return "."
        elif self.estado == Celula.VIVO:
            if self.generacion == 0:
                color = Colores.VERDE
            elif self.generacion == 1:
                color = Colores.AMARILLO
            elif self.generacion > 1:
                color = Colores.ROJO
            return f"{color}█{Colores.FIN}"
