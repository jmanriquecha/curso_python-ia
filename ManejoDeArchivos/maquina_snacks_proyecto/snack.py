class Snack:

    __contador_snacks = 0

    def __init__(self, nombre, precio):
        Snack.__contador_snacks += 1
        self.__id_snack = Snack.__contador_snacks
        self._nombre = nombre
        self._precio = precio


    @property
    def id_snack(self):
        return self.__id_snack


    @property
    def nombre(self):
        return self._nombre


    @property
    def precio(self):
        return self._precio


    def __str__(self):
        return f"Snack # {self.id_snack} - Snack: {self.nombre} - Precio: ${self.precio:.2f}"


    def escribir_snack(self):
        return f'{self.id_snack},{self.nombre},{self.precio}'

# Pruebas
if __name__ == "__main__":
    snack1 = Snack("Papas", 2500)
    print(snack1)
    snack2 = Snack("Gaseosa", 3000)
    print(snack2)

