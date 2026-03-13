from SistemaBiblioteca.Biblioteca import Biblioteca
from SistemaBiblioteca.Libro import Libro

def main():
    print("Sistema de Bibliotecas")
    nuevo_leon = Biblioteca("Nuevo León")
    libro1 = Libro("cien años de soledad", "Gabriel García Márquez", "drama")
    libro2 = Libro("los simson", "homero", "drama")
    libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
    libro4 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela clásica")
    libro5 = Libro("1984", "George Orwell", "Distopía")
    libro6 = Libro("Rebelión en la granja", "George Orwell", "Sátira política")
    libro7 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula")
    libro8 = Libro("La sombra del viento", "Carlos Ruiz Zafón", "Misterio")
    libro9 = Libro("Crónica de una muerte anunciada", "Gabriel García Márquez", "Novela")
    libro10 = Libro("El nombre de la rosa", "Umberto Eco", "Misterio histórico")
    libro11 = Libro("Drácula", "Bram Stoker", "Terror")
    libro12 = Libro("Frankenstein", "Mary Shelley", "Ciencia ficción")
    libro13 = Libro("Orgullo y prejuicio", "Jane Austen", "Romance")
    libro14 = Libro("El señor de los anillos", "J. R. R. Tolkien", "Fantasía")
    libro15 = Libro("Harry Potter y la piedra filosofal", "J. K. Rowling", "Fantasía")
    libro16 = Libro("Los juegos del hambre", "Suzanne Collins", "Distopía")
    libro17 = Libro("La metamorfosis", "Franz Kafka", "Ficción")
    libro18 = Libro("El código Da Vinci", "Dan Brown", "Suspenso")
    libro19 = Libro("It", "Stephen King", "Terror")
    libro20 = Libro("El alquimista", "Paulo Coelho", "Ficción filosófica")
    libro21 = Libro("La isla del tesoro", "Robert Louis Stevenson", "Aventura")
    libro22 = Libro("Viaje al centro de la Tierra", "Julio Verne", "Ciencia ficción")

    # Agregar libros a la biblioteca
    libros = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10,
              libro11, libro12, libro13, libro14, libro15, libro16, libro17, libro18, libro19, libro20, libro21, libro22]

    for libro in libros:
        nuevo_leon.agregar_libro(libro)

    nuevo_leon.buscar_libros_por_autor("Gabriel García Márquez")
    nuevo_leon.buscar_libros_por_genero("terror")
    nuevo_leon.buscar_un_libro_por_titulo("Los juegos del hambre")
    nuevo_leon.mostrar_todos_los_libros()

if __name__ == "__main__":
    main()
