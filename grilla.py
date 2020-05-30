from celula import CelulaFactory, CelulaViva


class Grilla:
    def __init__(self, estado_inicial, ancho, alto):
        self.celdas = estado_inicial
        self.ancho = ancho
        self.alto = alto
        self.generacion = 0

    @classmethod
    def desdeAnchoAlto(clase, ancho, alto):
        return clase([
            [
                CelulaFactory.obtener()
                for _ in range(ancho)
            ]
            for _ in range(alto)
        ], ancho, alto)

    @classmethod
    def desdeEstadoInicial(clase, estado_inicial):
        ancho = len(estado_inicial[0])
        alto = len(estado_inicial)

        return clase([
            [
                CelulaFactory.obtener(estado_inicial[y][x])
                for x in range(ancho)
            ]
            for y in range(alto)
        ], ancho, alto)

    def avanzar(self):
        def contar_vecinos(vecino):
            return estado_anterior[vecino[1]][vecino[0]].conteo()

        estado_anterior = [
            [celula for celula in fila]
            for fila in self.celdas
        ]

        for x in range(self.ancho):
            for y in range(self.alto):
                celula = self.celdas[y][x]
                vecinos_vivos = sum(map(contar_vecinos, self.vecinos(x, y)))
                self.celdas[y][x] = celula.avanzar(vecinos_vivos)

        self.generacion += 1

    def dibujar(self):
        salida = f"Generacion: {self.generacion}\n╭{'─' * self.ancho}╮\n"

        for fila in self.celdas:
            salida = f"{salida}│{''.join([celula.dibujar() for celula in fila])}│\n"

        return f"{salida}╰{'─' * self.ancho}╯\n"

    def esta_vacio(self):
        return not any([any([type(celula) == CelulaViva for celula in fila]) for fila in self.celdas])

    def vecinos(self, x, y):
        for diff_x in (-1, 0, 1):
            for diff_y in (-1, 0, 1):
                x2 = x + diff_x
                y2 = y + diff_y
                if (0 <= x2 < self.ancho) and (0 <= y2 < self.alto) and not(x2 == x and y2 == y):
                    yield (x2, y2)
