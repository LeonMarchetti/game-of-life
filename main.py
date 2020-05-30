from time import sleep

from grilla import Grilla


def main():
    if 0:
        grilla = Grilla.desdeAnchoAlto(8, 5)
    else:
        estado_inicial = [
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]
        ]
        grilla = Grilla.desdeEstadoInicial(estado_inicial)

    while True:
        print(grilla.dibujar())
        if grilla.esta_terminado():
            break
        sleep(1)
        grilla.avanzar()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
