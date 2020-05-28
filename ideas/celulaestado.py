class CelulaEstado:
    def avanzar(self, vecinos_vivos):
        pass

    def dibujar(self):
        pass

    def conteo(self):
        pass


class CelulaEstadoVivo(CelulaEstado):
    def avanzar(self, vecinos_vivos):
        if (vecinos_vivos < 2 or vecinos_vivos > 3):
            return CelulaEstadoMuerto()
        return self

    def dibujar(self):
        return "█"

    def conteo(self):
        return 1


class CelulaEstadoMuerto(CelulaEstado):
    def avanzar(self, vecinos_vivos):
        if (vecinos_vivos == 3):
            return CelulaEstadoVivo()
        return self

    def dibujar(self):
        return "."

    def conteo(self):
        return 0


class CelulaEstadoFactory(object):
    @staticmethod
    def obtener(estado):
        if (estado == 0):
            return CelulaEstadoMuerto()
        elif (estado == 1):
            return CelulaEstadoVivo()
        return None
