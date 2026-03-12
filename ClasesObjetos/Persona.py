class Persona:

    # Inicializa atributos
    def __init__(self, nombre, apellido, anio_nacido):
        self.nombre = nombre
        self.apellido = apellido
        self.anio_nacido = int(anio_nacido)

    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'

    def edad(self):
        return 2026 - self.anio_nacido

    def mostrar_direccion_memoria(self):
        print(f"direccioón en memoria {id(self)}")
        print(f"direccioón en memoria exadecimal {hex(id(self))}")
        print()


if __name__ == "__main__":
    persona1 = Persona("Carlos", "Carrillo", 1992)
    print(f"{persona1.nombre_completo()} tienes {persona1.edad()} años")
    persona1.mostrar_direccion_memoria()
    # imprimir la dirección en memoria
    print(f"direccioón en memoria {id(persona1)}")
    print(f"direccioón en memoria exadecimal {hex(id(persona1))}")

    persona2 = Persona("José", "Martinez", 1975)
    print(f"{persona2.nombre_completo()} tienes {persona2.edad()} años")
    persona1.mostrar_direccion_memoria()
    print(f"direccioón en memoria {id(persona1)}")
    print(f"direccioón en memoria exadecimal {hex(id(persona1))}")
