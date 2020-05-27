from time import sleep

from grilla import Grilla


def main():
    grilla = Grilla(8, 5)
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
