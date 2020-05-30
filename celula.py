from random import getrandbits

from colores import Colores


class Celula:
    def avanzar(self, vecinos_vivos):
        pass

    def dibujar(self):
        pass


class CelulaViva(Celula):
    def __init__(self):
        self.generacion = 0

    def avanzar(self, vecinos_vivos):
        if (2 <= vecinos_vivos <= 3):
            self.generacion += 1
            return self
        else:
            return CelulaMuerta()

    def conteo(self):
        return 1

    def dibujar(self):
        if (self.generacion == 0):
            color = Colores.VERDE
        elif (self.generacion == 1):
            color = Colores.AMARILLO
        elif (self.generacion > 1):
            color = Colores.ROJO
        return f"{color}█{Colores.FIN}"


class CelulaMuerta(Celula):
    def avanzar(self, vecinos_vivos):
        if (vecinos_vivos == 3):
            return CelulaViva()
        return self

    def conteo(self):
        return 0

    def dibujar(self):
        return "."


class CelulaFactory:
    @staticmethod
    def obtener(estado_inicial=None):
        estado = estado_inicial if (
            estado_inicial is not None) else getrandbits(1)

        if (estado == 0):
            return CelulaMuerta()
        elif (estado == 1):
            return CelulaViva()
        else:
            raise ValueError("Valor inválido para estado de célula.")
