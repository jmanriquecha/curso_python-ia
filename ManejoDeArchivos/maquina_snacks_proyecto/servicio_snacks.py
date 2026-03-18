import os.path

from maquina_snacks_proyecto.snack import Snack


class ServicioSnacks:

    NOMBRE_ARCHIVO = 'snacks.txt'

    def __init__(self):
        self._snacks  = []
        # Revisamos si ya existe el archivo snacks.txt
        # Si ya existe obtenemos los snacks del archivo
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self._snacks = self.obtener_snacks()
        # Sí no existe agregamos unos snacks iniciales
        else:
            self.cargar_snacks_iniciales()


    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Papas', 20.5),
            Snack('Gaseosa', 25.5),
            Snack('Jugo', 10.5)
        ]
        self.snacks.extend(snacks_iniciales) # Se agregan los snacks iniciales a la lista snacks
        # Se guarda información en archivo
        self.guardar_snack_archivo(snacks_iniciales)


    def guardar_snack_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f'Error al guardar snacks en el archivo {e}\n')


    def obtener_snacks(self):
        snacks = []

        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    id_snack, nombre, precio = linea.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
        except Exception as e:
            print(f"Error al leer el archivo de snacks {e}")
        return snacks


    def agregar_snack(self, snack):
        self._snacks.append(snack)
        self.guardar_snack_archivo([snack])


    def mostrar_snacks(self):
        print("--- Snacks en el inventario ---")
        for snack in self.get_snacks():
            print(snack)


    def get_snacks(self):
        return self._snacks


    def __str__(self):
        snack_str = ''

        for snack in self.snacks:
            snack_str += '\n' + snack.__str__()

        return f'''Lista de Snacks
            {snack_str}'''


# Prueba
if __name__ == '__main__':
    snack1 = Snack('frutas', 20.2)

    servicio_snack1 = ServicioSnacks()
    # servicio_snack1.snacks = snack1
    # print(servicio_snack1)
    servicio_snack1.mostrar_snacks()
