from celula import Celula


class Grilla:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.celdas = [[Celula() for _ in range(self.ancho)] for _ in range(self.alto)]
        self.generacion = 0

    def avanzar(self):
        def contar_vecinos(vecino):
            return 1 if (estado_anterior[vecino[1]][vecino[0]] == Celula.VIVO) else 0

        estado_anterior = [[celula.estado for celula in fila] for fila in self.celdas]

        for x in range(self.ancho):
            for y in range(self.alto):
                celula = self.celdas[y][x]
                vecinos_vivos = sum(map(contar_vecinos, self.vecinos(x, y)))
                celula.avanzar(vecinos_vivos)

        self.generacion += 1

    def dibujar(self):
        print(f"Generacion: {self.generacion}")
        print("╭" + "─" * self.ancho + "╮")

        for columna in self.celdas:
            print("│", end="")
            for celula in columna:
                print(celula.dibujar(), end="")
            print("│")

        print("╰" + "─" * self.ancho + "╯")

    def esta_terminado(self):
        for fila in self.celdas:
            for celula in fila:
                if celula.estado == Celula.VIVO:
                    return False
        return True

    def vecinos(self, x, y):
        for diff_x in (-1, 0, 1):
            for diff_y in (-1, 0, 1):
                x2 = x + diff_x
                y2 = y + diff_y
                if (0 <= x2 < self.ancho) and (0 <= y2 < self.alto) and not(x2 == x and y2 == y):
                    yield (x2, y2)
