print("Boletin de suscriptores")

suscriptores = set()

menu = """
Administración de suscriptores
    1. Agregar suscriptor
    2. Eliminar suscriptor
    3. Consultar suscriptores
    0. Salir
    
Elije una opción: """

while True:
    try:
        opcion = int(input(menu))
    except ValueError:
        print("Ingresa una opción válida (Las opciones del menú)" )
        continue

    match opcion:
        case 0:
            print("Saliendo del sistema...")
            break
        case 1:
            email = input("Ingresa el email para notificar: ")
            suscriptores.add(email)
        case 2:
            email = input("Ingresa el email que desea eliminar: ")
            suscriptores.discard(email)
        case 3:
            print("--- Suscriptores Activos ---")
            if suscriptores:
                for mail in sorted(suscriptores):
                    print(f"- {mail}")
            else:
                print("No hay suscriptores en el momento!")
        case _:
            print("Opción no válida! ")
