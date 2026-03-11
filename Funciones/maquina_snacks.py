print("*** Maquina de Snacks ***")
#"""
snacks = [
    {"snack_id": 1, "nombre": "papas", "precio": 20.5, "cantidad": 100},
    {"snack_id": 2, "nombre": "gaseosa", "precio": 30.33, "cantidad": 100},
    {"snack_id": 3, "nombre": "jugo", "precio": 12.66, "cantidad": 100},
    {"snack_id": 4, "nombre": "galletas", "precio": 6.55, "cantidad": 100},
    {"snack_id": 5, "nombre": "agua", "precio": 25.02, "cantidad": 100}
]
#"""

#snacks = []

snacks_comprados = []


def mostrar_snacks(lista_snacks):
    if lista_snacks:
        print("Listado de Snacks en stock")
        for snack in lista_snacks:
            if snack['cantidad'] > 0: # Solo se deben mostrar los snacks cuando tengan stock mayor que 0
                print(f"""-> Id: {snack['snack_id']}, Nombre: {snack['nombre']}, Precio: ${snack['precio']:.2f}, Stock: {snack['cantidad']}""")
    else:
        print("En el momento no se han agregado Snacks, intente más tarde!")


def comprar_snacks(snack_id):
    snack_encontrado = buscar_id(snack_id)
    if snack_encontrado:
        if snack_encontrado['cantidad'] > 0:
            agregar_snack = {
                'snack_id': snack_encontrado['snack_id'],
                'nombre': snack_encontrado['nombre'],
                'precio': snack_encontrado['precio']
            }
            # Descontar snack del snacks
            snack_encontrado['cantidad'] -= 1
            snacks_comprados.append(agregar_snack)
            print(f"Snack agregado correctamente: {snack_encontrado['nombre']}")
        else:
            print(f"Lo sentimos, en este momento no tenemos disponibilidad del snack solicitado con id {snack_encontrado['snack_id']}")
    else:
        print("No hay snacks agregados a la maquina en el momento!")


def mostrar_ticket():
    total = 0
    if snacks_comprados:
        print(":::::::::::Ticket de venta::::::::::::::")
        for snack in snacks_comprados:
            print(f"""- ID: {snack['snack_id']} -> Nombre: {snack['nombre']} | Precio: ${snack['precio']:.2f}""")
            total += snack['precio'] # Contabiliza el total a pagar

        print(f"\n=> Valor total: ${total:.2f}")
    else:
        print("¡Aún no haz agregado snacks al carrito!")


def buscar_id(snack_id):
    for snack in snacks:
        if snack_id == snack["snack_id"]:
            return  snack
    return None


def mostrar_menu():
    menu = """
    ::::::::::::::::::::::::::::::::::::::::::::
    --- Maquina de Snacks ---
    ::::::::::::::::::::::::::::::::::::::::::::
        1. Mostrar Snacks
        2. Comprar Snacks
        3. Mostrar Ticket
        0. Salir
        
    Selección una opción númerica del menú
    ---------------------------------------------
    """

    while True:

        try:
            opcion = int(input(menu))
        except ValueError:
            print("Ingresa un valor numérico")
            continue

        match opcion:
            case 0:
                print("Saliendo del sistema, hasta pronto!")
                break

            case 1:
                mostrar_snacks(snacks)

            case 2:
                if snacks:
                    buscar_snack = int(input("Ingrese el id del snack que desea comprar: "))
                    comprar_snacks(buscar_snack)
                else:
                    print("No hay snacks agregados en la maquina en el momento! intenta más tarde")

            case 3:
                mostrar_ticket()


            case _:
                print("La opción seleccionada no es válida, por favor verifica e intenta de nuevo!")

if __name__ == "__main__":
    mostrar_menu()