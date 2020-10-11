# from celula import Celula

class Regla:
    @staticmethod
    def aplicar(params):
        pass


class ReglaConway(Regla):
    @staticmethod
    def aplicar(params):
        # params: { estado: int, vecinos: int}
        if (params["estado"]):
            if (2 <= params["vecinos"] <= 3):
                return 1
        else:
            if (params["vecinos"] == 3):
                return 1
        return 0


class Regla110(Regla):
    @staticmethod
    def aplicar(params):
        # params: { prev: int, cur: int, post: int }
        A = params["prev"] == 1
        B = params["cur"] == 1
        C = params["post"] == 1

        Y = (not A and C) or (not B and C) or (B and not C)
        return 1 if Y else 0


class Regla30(Regla):
    @staticmethod
    def aplicar(params):
        # params: { prev: int, cur: int, post: int }
        A = params["prev"] == 1
        B = params["cur"] == 1
        C = params["post"] == 1

        Y = A != (B or C)
        return 1 if Y else 0


class ReglaBrianBrain(Regla):
    @staticmethod
    def aplicar(params):
        # params: { estado: int, vecinos: int}
        if (params["estado"] == 0): # off
            if (params["vecinos"] == 2):
                return 2
            else:
                return 0
        elif (params["estado"] == 1): # dying
            return 0
        elif (params["estado"] == 2): # on
            return 1
        else:
            raise ValueError()
