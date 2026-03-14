from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Orden:

    __contador_ordenes = 0

    def __init__(self, computadoras=None):
        Orden.__contador_ordenes += 1
        self.__id_orden = self.contador_ordenes()
        self._computadoras = computadoras if computadoras else []


    @classmethod
    def contador_ordenes(cls):
        return cls.__contador_ordenes


    @property
    def id_orden(self):
        return self.__id_orden


    @property
    def computadoras(self):
        return self._computadoras


    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)


    def __str__(self):
        computadoras_str = ''

        for computadora in self.computadoras:
            computadoras_str += '\n' + computadora.__str__()

        return f"""Orden: {self.id_orden}
        Computadoras: {computadoras_str}"""


if __name__ == "__main__":
    raton1 = Raton('genius', 'usb')
    teclado1 = Teclado('hp', 'usb')
    monitor1 = Monitor('Samsung', 30)
    computadora1 = Computadora('LG', monitor1, teclado1, raton1)

    orden1 = Orden()
    orden1.agregar_computadora(computadora1)
    print(orden1)