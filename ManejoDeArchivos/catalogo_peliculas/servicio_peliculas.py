import os.path

from catalogo_peliculas.pelicula import Pelicula


class ServicioPeliculas:

    NOMBRE_ARCHIVO = 'peliculas.txt'

    def __init__(self):
        self._peliculas = []

        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self._peliculas = self.obtener_peliculas()


    @property
    def peliculas(self):
        return self._peliculas


    @peliculas.setter
    def peliculas(self, pelicula):
        self.peliculas.append(pelicula)


    def obtener_peliculas(self):
        peliculas = []

        try:
           with open(self.NOMBRE_ARCHIVO, 'r', encoding='utf8') as archivo:
               for linea in archivo:
                   nombre = linea.strip()
                   pelicula = Pelicula(nombre)
                   peliculas.append(pelicula)
        except Exception as e:
           print(f'Ocurrio un error al obtener las peliculas: {e}')

        return peliculas


    def agregar_pelicula(self, pelicula):
        self.peliculas = pelicula
        self.guardar_pelicula_archivo([pelicula])


    def guardar_pelicula_archivo(self, peliculas):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a', encoding='utf8') as archivo:
                for pelicula in peliculas:
                    archivo.write(f'{pelicula.escribir_pelicula()}\n')
        except Exception as e:
            print(f'Ocurrio un error al guardar la pelicula en el archivo: {e}')


    def listar_peliculas(self):
        print('--- Catalogo de películas ---')
        if self.peliculas:
            for pelicula in self.peliculas:
                print(pelicula)
        else:
            print("No hay peliculas en el catalogo")


    def eliminar_archivo_catalogo(self):
        # Verificar si el archivo existe antes de borrarlo
        if os.path.exists(self.NOMBRE_ARCHIVO):
            os.remove(self.NOMBRE_ARCHIVO)
            self.peliculas.clear() # Se elimina catalogo de la lista
            print(f'Archivo Eliminado!')
        else:
            print('El archivo no existe!')


if __name__ == '__main__':
    pelicula1 = Pelicula('Furia de titanes')
    #
    servicio_peliculas = ServicioPeliculas()
    # servicio_peliculas.agregar_pelicula(pelicula1)
    servicio_peliculas.listar_peliculas()
    servicio_peliculas.eliminar_archivo_catalogo()

