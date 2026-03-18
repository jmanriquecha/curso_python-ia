import inspect

from maquina_snacks_proyecto.servicio_snacks import ServicioSnacks
from maquina_snacks_proyecto.snack import Snack


class MaquinaSnacks:

    def __init__(self):
        self._servicios_snacks = ServicioSnacks()
        self._productos = []


    @property
    def servicios_snacks(self):
        return self._servicios_snacks


    @property
    def productos(self):
        return self._productos


    def maquina_snacks(self):
        salir = False

        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Ocurrio un error: {e}")


    def mostrar_menu(self):
        menu = """------ Menu principal ------
        1. Comprar Snack
        2. Mostrar Ticket
        3. Agregar Nuevo Snack al Inventario
        4. Mostrar Inventario Snacks
        0. Salir"""
        print('\n' + inspect.cleandoc(menu) + '\n')
        return int(input('Elige una opción: '))

    def ejecutar_opcion(self,opcion):
        print("Ejecutando opción")
        if opcion == 0:
            print('Saliendo del sistema...')
            return True

        match opcion:
            case 1:
                self.comprar_snack()
            case 2:
                self.mostrar_ticket()
            case 3:
                self.agregar_snack()
            case 4:
                self.servicios_snacks.mostrar_snacks()
            case _:
                print('Opción invalida!')

        return False


    def comprar_snack(self):
        id_snack = int(input('¿Qué Snack quieres comprar? ingresa el ID: '))
        snacks = self.servicios_snacks.get_snacks()
        snack = next((snack for snack in snacks if id_snack == snack.id_snack), None)

        if snack:
            self.productos.append(snack)
            print(f'Snack encontrado {snack}')
        else:
            print(f'Id Snack no encontrado {id_snack}')


    def mostrar_ticket(self):
        if not self.productos:
            print("No hay productos en el ticket")
            return

        total = sum(snack.precio for snack in self.productos)

        print(':::: Ticket de Venta ::::')

        for producto in self.productos:
            print(f'-> {producto.nombre} - ${producto.precio:.2f}')

        print(f'Total: ${total:.2f}')


    def agregar_snack(self):
        nombre = input("Ingresa el nombre del snack: ")
        precio = float(input("Ingresa el precio del snack: $"))

        snack = Snack(nombre, precio)

        # Agregar Snack
        self.servicios_snacks.agregar_snack(snack)


# Prueba
if __name__ == '__main__':
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()
