class CelulaEstado:
    @staticmethod
    def avanzar(vecinos_vivos):
        pass

    @staticmethod
    def dibujar():
        pass

    @staticmethod
    def conteo_vecino():
        pass

class CelulaEstadoVivo(CelulaEstado):
    @staticmethod
    def avanzar(vecinos_vivos):
        if 2 > vecinos_vivos > 3:
            return CelulaEstadoMuerto
        return CelulaEstadoVivo

    @staticmethod
    def dibujar():
        return "█"

    @staticmethod
    def conteo_vecino():
        return 1


class CelulaEstadoMuerto(CelulaEstado):
    @staticmethod
    def avanzar(vecinos_vivos):
        if vecinos_vivos == 3:
            return CelulaEstadoVivo
        return CelulaEstadoMuerto

    @staticmethod
    def dibujar():
        return "."

    @staticmethod
    def conteo_vecino():
        return 0


class CelulaEstadoFactory(object):
    @staticmethod
    def obtener(estado):
        if estado == 0:
            return CelulaEstadoMuerto
        elif estado == 1:
            return CelulaEstadoVivo
        else:
            return CelulaEstado
