print("### Gestión de Inventarios ###")

# Crear lista para mantener el registro de los productos disponibles en el almacen

inventario = []

# Crear menu
menu = """
Menu principal de gestión de inventarios
    1. Agregar nuevo producto
    2. Buscar producto
    3. Imprimir productos
    0. Salir
    
Elige una opción valida: """

while True:
    try:
        opcion = int(input(menu))
    except ValueError:
        print("Solo debe seleccionar un opción númerica del menu: ")
        continue

    match opcion:
        case 0:
            print("Saliendo del sistema, hasta pronto...")
            break
        case 1:
            # Detalle del producto codigo, nombre, precio y cantidad disponible
            codigo = input("Ingresa el código del producto: ")

            existe = False
            for producto in inventario:
                if producto["codigo"] == codigo:
                    existe = True
                    break

            if existe:
                print("Ya existe un producto con ese código")
                continue

            nombre = input("Ingresa el nombre del producto: ")
            try:
                precio = float(input("Ingresa el precio del producto: $"))
                cantidad = int(input("Ingresa la cantidad de productos: "))
            except ValueError:
                print("Precio y cantidad solo deben ser numericos")
                continue

            if precio <= 0 or cantidad <= 0:
                print("Valores invalidos")
                continue

            detalle = {
                "codigo":codigo,
                "nombre":nombre,
                "precio":precio,
                "cantidad":cantidad
            }

            # Agrega el detalle del nuevo producto
            inventario.append(detalle)
            print(f"El producto {nombre} se agrego correctamente!")
        case 2:
            encontrado = False
            # Busca producto
            buscar = input("Ingresa el código del producto que desea buscar: ")
            for producto in inventario:
                if buscar == producto["codigo"]:
                    print(f"""--- Detalle del producto Código: << {producto['codigo']} >> ---
    Nombre: {producto['nombre']}
    Precio ${producto['precio']:.2f}
    Cantidad: {producto['cantidad']:.0f}""")
                    encontrado = True
                    break

            if not encontrado:
                print("El producto no fue encontrado!")

        case 3:
            #Imprimir productos
            if inventario:
                for producto in inventario:
                    print(f"""--- Detalle del producto ID: << {producto['codigo']} >> ---
    Nombre: {producto['nombre']}
    Precio ${producto['precio']:.2f}
    Cantidad: {producto['cantidad']:.0f}
""")
            else:
                print("No hay productos en inventario")
