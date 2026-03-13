class Persona:

    _contador_personas = 0

    def __init__(self, nombre, apellido):
        Persona._contador_personas += 1
        self.__id = self.cuenta_personas_cls()
        self._nombre = nombre
        self._apellido = apellido

    """@staticmethod
    def cuenta_personas_static():
        return  Persona._contador_personas"""

    @classmethod
    def cuenta_personas_cls(cls):
        return cls._contador_personas

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_apellido(self):
        return self._apellido

    def get_nombre_completo(self):
        return f"{self._nombre} {self._apellido}"

    def imprime_tarjeta(self):
        print(f"Id: {self.__id} - Nombre y apellidos {self.get_nombre_completo()}")

if __name__ == "__main__":
    persona1 = Persona('Carlos', 'Restrepo')
    persona1.imprime_tarjeta()

    persona2 = Persona('Xiomara', 'Castro')
    persona2.imprime_tarjeta()

    persona3 = Persona('Aida', 'Chavez')
    persona3.imprime_tarjeta()

    #print(f"Total personas {Persona._contador_personas}")
    #print(f"Total personas con metodo static {Persona.cuenta_personas_static()}")
    print(f"Total personas con metodo class {Persona.cuenta_personas_cls()}") #Esta es la forma recomendada por python
