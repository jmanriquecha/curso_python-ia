class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color
        #self.marca = marca # Atributo público
        #self._modelo = modelo # _ Atributo Protegido
        #self.__color = color # __ Atributo privado

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def conducir(self):
        print(f"""Conduciendo coche
    Marca: {self._marca}
    Modelo: {self._modelo}
    Color: {self._color}""")

if __name__ == "__main__":
    # Esto no se debe hacer
    """
    mazda = Coche("Mazda", "2026", "Rojo")
    mazda.marca = "Renault"
    mazda._modelo = 2020
    mazda.__color = "Verde"
    mazda.conducir()
    
    nissan = Coche("Nissan", "2026", "Rojo")
    nissan.conducir()
    """

    mazda = Coche("Mazda", 2026, "Amarillo")
    mazda.set_color("Red")
    mazda.conducir()