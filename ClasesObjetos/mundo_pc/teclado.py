from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    __contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.__contador_teclados += 1
        self.__id_teclado = self.contador_teclados()
        super().__init__(marca, tipo_entrada)


    @property
    def id_teclado(self):
        return self.__id_teclado


    @classmethod
    def contador_teclados(cls):
        return cls.__contador_teclados


    def __str__(self):
        return f'Teclado -> ID: {self.__id_teclado}  Marca: {self.marca} Tipo de Entrada: {self.tipo_entrada}'