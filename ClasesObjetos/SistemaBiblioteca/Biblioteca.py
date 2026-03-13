from SistemaBiblioteca.Libro import Libro


class Biblioteca:

    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []


    def agregar_libro(self, libro):
        libro = libro
        self._libros.append(libro)


    def buscar_libros_por_autor(self, autor):
        print(f"\nMostrando libro del autor < {autor} >")
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                print(libro)


    def buscar_libros_por_genero(self, genero):
        print(f"\nMostrando libro del genero < {genero} >")
        for libro in self._libros:
            if libro.genero.lower() == genero.lower():
                print(libro)


    def mostrar_todos_los_libros(self):
        print("\nMostrando todos los libros")
        for libro in self._libros:
            print(libro)


    def buscar_un_libro_por_titulo(self, titulo):
        print(f"\nMostrando libro por título")
        for libro in self._libros:
            if libro.titulo.lower() == titulo.lower():
                print(libro)

