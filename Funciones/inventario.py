print('Sistema de inventario')

inventario = []

def agregar_producto(producto_id, nombre, precio, cantidad):
    producto = {"producto_id" : producto_id, "nombre":nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)


def buscar_producto(producto_id):
    for producto in inventario:
        if producto_id == producto['producto_id']:
            return producto
    return None


def mostrar_productos(arr):
    if arr:
        print("Detalle de los Productos encontrados...\n")
        for producto in arr:
            print(
                f"ID: {producto['producto_id']}\n"
                f" Nombre: {producto['nombre']}\n"
                f" Precio: ${producto['precio']:.2f}\n"
                f" Cantidad: {producto['cantidad']}\n")
    else:
        print("No hay productos disponibles para mostrar. ")


def generaIdUnico():
    nuevo_id = 1
    while buscar_producto(nuevo_id):
        nuevo_id += 1
    return nuevo_id


def menu_principal():
    menu = """
    Menú principal de gestión de inventarios
        1. Agregar productos
        2. Buscar porducto por Id
        3. Mostrar inventario
        0. Salir
        
    Elige una opción: """

    while True:
        try:
            opcion = int(input(menu))
        except ValueError:
            print("Solo se permiten valores númericos")
            continue

        match opcion:
            case 0:
                print("Saliendo del sistema...")
                break
            case 1:
                producto_id = generaIdUnico()

                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: $"))
                cantidad = int(input("Ingrese la cantida del producto: "))
                agregar_producto(producto_id, nombre, precio, cantidad)

                print(f"El producto {nombre} se agrego correctamente.")
            case 2:
                producto_id = int(input("Ingrese el ID del producto: "))
                producto = buscar_producto(producto_id)

                if producto:
                    print(
                        f"Detalle del Producto encontrado...\n"
                        f"ID: {producto['producto_id']}\n"
                        f" Nombre: {producto['nombre']}\n"
                        f" Precio: ${producto['precio']:.2f}\n"
                        f" Cantidad: {producto['cantidad']}\n")
                else:
                    print("No se encontraron resultados")
            case 3:
                mostrar_productos(inventario)
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    menu_principal()
