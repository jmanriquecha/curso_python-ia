import inspect

from catalogo_peliculas.pelicula import Pelicula
from catalogo_peliculas.servicio_peliculas import ServicioPeliculas


class AppCatalogoPeliculas:

    def __init__(self):
        self._servicio_peliculas = ServicioPeliculas()


    @property
    def servicio_peliculas(self):
        return self._servicio_peliculas


    def muestra_menu(self):
        salir = False

        while not salir:
            try:
                opcion_menu = self.menu()
                salir = self.ejecuta_opcion(opcion_menu)
            except ValueError:
                print(f"Ocurrio un error: Solo se puede ingresar valores numéricos: ")


    def menu(self):
        menu = """
        1. Agregar Pelicula
        2. Listar Peliculas
        3. Eliminar Catalogo de Peliculas
        0. Salir"""
        print(f'\n{inspect.cleandoc(menu)}\n')
        opcion = int(input("Ingresa una opción (0 -4): "))
        return opcion


    def ejecuta_opcion(self, opcion):
        if opcion == 0:
            print("Saliendo del sistema...")
            return True

        match opcion:
            case 1:
                self.agregar_pelicula()
            case 2:
                self.listar_peliculas()
            case 3:
                self.eliminar_catalogo_peliculas()
            case _:
                print(f"Opción no válida: {opcion}")
        return False


    def agregar_pelicula(self):
        nombre = input("Ingresa el nombre de la pelicula: ")
        nueva_pelicula = Pelicula(nombre)
        self.servicio_peliculas.agregar_pelicula(nueva_pelicula)


    def listar_peliculas(self):
        self.servicio_peliculas.listar_peliculas()


    def eliminar_catalogo_peliculas(self):
        self.servicio_peliculas.eliminar_archivo_catalogo()

if __name__ == '__main__':
    app_catalogo_peliculas = AppCatalogoPeliculas()
    app_catalogo_peliculas.muestra_menu()