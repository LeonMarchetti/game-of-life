class CelulaEstado(object):
    @staticmethod
    def avanzar(vecinos_vivos):
        pass

    @staticmethod
    def dibujar():
        pass

class CelulaEstadoVivo(CelulaEstado):
    @staticmethod
    def avanzar(vecinos_vivos):
        super().avanzar(vecinos_vivos)
        if 2 > vecinos_vivos > 3:
            return CelulaEstadoMuerto()
        return None

    @staticmethod
    def dibujar():
        return "█"


class CelulaEstadoMuerto(CelulaEstado):
    @staticmethod
    def avanzar(vecinos_vivos):
        super().avanzar(vecinos_vivos)
        if vecinos_vivos == 3:
            return CelulaEstadoVivo()
        return None

    @staticmethod
    def dibujar():
        return "."


class CelulaEstadoFactory(object):
    @staticmethod
    def obtener(estado):
        if estado == 0:
            return CelulaEstadoMuerto()
        elif estado == 1:
            return CelulaEstadoVivo()
        else:
            return CelulaEstado()
