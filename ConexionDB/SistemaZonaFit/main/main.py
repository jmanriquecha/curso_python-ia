import inspect
from os.path import join

from service.cliente_service import ClienteService

def menu():
    opciones_menu = """
    ::::::::::::::::::::::::::::::::
    1. Listar Clientes
    2. Buscar cliente por ID
    3. Agregar Cliente
    4. Modificar Cliente
    5. Eliminar Cliente
    0. Salir
    ::::::::::::::::::::::::::::::::"""
    print(f"\n{inspect.cleandoc(opciones_menu)}\n")
    return int(input("Ingresa una opción (0 - 5): "))


def mostrar_menu():
    salir = False
    print("### Sistema Zona Fit ###")
    while not salir:
        try:
            opcion = menu()
            salir = ejecuta_opciones(opcion)
        except Exception as e:
            print(f"Error: {e}")


def ejecuta_opciones(opcion):
    if opcion == 0:
        print("Saliendo del sistema...")
        return True

    match opcion:
        case 1:
            clientes = ClienteService()
            print("Listado de clientes")
            for cliente in clientes.listar_clientes():
                # print(f"-> {cliente.nombre}, {cliente.apellido}, {cliente.membresia}")
                print(cliente)

        case 2:
            cliente_id = int(input("Ingrese el ID del cliente: "))
            cliente = ClienteService()
            resultado = cliente.buscar_cliente_id(cliente_id)
            print(resultado)

        case 3:
            nombre = input("Ingresa el nombre: ")
            apellido = input("Ingresa el apellido: ")
            membresia = input("Ingresa la membresia: $")

            clientes_service = ClienteService()
            clientes_service.crear_cliente(nombre, apellido, membresia)

        case 4:
            clientes_service = ClienteService()

            cliente_id = int(input("Ingresa el id del cliente que va a modificar: "))
            cliente = clientes_service.editar_cliente(cliente_id)
            if cliente:
                print(f"Datos del cliente con id {cliente.cliente_id}")
                # print(f"-> {cliente.nombre}, {cliente.apellido}, {cliente.membresia}")
                print(cliente)

                nuevo_nombre = input("Ingresa el nuevo nombre: ")
                nuevo_apellido = input("Ingresa el nuevo apellido: ")
                nueva_membresia = input("Ingresa la nueva mebresia: $")

                clientes_service.actualizar_cliente(cliente_id, nuevo_nombre, nuevo_apellido, nueva_membresia)
            else:
                print(f"El cliente con {cliente_id} no existe!")

        case 5:
            clientes_service = ClienteService()
            cliente_id = int(input("Ingresa el ID del cliente que quiere eliminar: "))
            clientes_service.eliminar_cliente(cliente_id)


if __name__ == '__main__':
    mostrar_menu()