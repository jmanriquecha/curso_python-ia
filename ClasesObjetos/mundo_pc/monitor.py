class Monitor:

    __contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.__contador_monitores += 1
        self.__id_monitor = self.contador_monitores()
        self._marca = marca
        self._tamanio = tamanio


    @property
    def id_monitor(self):
        return self.__id_monitor


    @property
    def marca(self):
        return self._marca


    @marca.setter
    def marca(self, marca):
        self._marca = marca


    @property
    def tamanio(self):
        return self._tamanio


    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio


    @classmethod
    def contador_monitores(cls):
        return Monitor.__contador_monitores


    def __str__(self):
        return f'Monitor -> ID: {self.id_monitor} Marca: {self.marca} Tamaño: {self.tamanio}'


