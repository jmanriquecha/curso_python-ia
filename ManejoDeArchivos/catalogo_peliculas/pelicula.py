class Pelicula:

    def __init__(self, nombre):
        self._nombre = nombre


    @property
    def nombre(self):
        return self._nombre


    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    def escribir_pelicula(self):
        return f'{self.nombre}'


    def __str__(self):
        return f'> {self.nombre}'