from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    __contador_ratones = 0


    def __init__(self, marca, tipo_entrada):
        Raton.__contador_ratones += 1
        self.__id_raton = self.contador_ratones()
        super().__init__(marca, tipo_entrada)


    @property
    def id_raton(self):
        return self.__id_raton


    @classmethod
    def contador_ratones(cls):
        return cls.__contador_ratones


    def __str__(self):
        return f'Raton -> ID: {self.id_raton} Marca: {self.marca} Tipo de Entrada: {self.tipo_entrada}'