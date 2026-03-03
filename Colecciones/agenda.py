print("### Agenda de contactos ###")

agenda = {}

menu = """
Menu principal - Agenda de contactos
    1. Agregar contacto
    2. Modificar contacto
    3. Eliminar contacto
    4. Listar contactos
    0. Salir
    
Escoge un opción: """

while True:
    try:
        opcion = int(input(menu))
    except ValueError:
        print("Opción inválida!")
        continue

    match opcion:
        case 0:
            print("Saliendo del sistema...")
            break
        case 1:
            nombre = input("Ingresa el nombre: ")
            telefono = input("Ingresa el telefono: ")
            email = input("Ingresa el email: ")
            direccion = input("Ingresa la dirección: ")

            agenda[nombre] = {
                "telefono": telefono,
                "email": email,
                "direccion": direccion
            }
            print(f"Contacto {nombre}, agregado correctamente.")
        case 2:
            contacto = input("Ingresa el nombre del contacto que desea modificar: ")
            if contacto in agenda:
                try:
                    opcion_modificar = int(input("""
                    Selecciona que desea modificar:
                        1. Teléfono
                        2. Email
                        3. Dirección
                        0. Volver al menú anterior"""))
                except ValueError:
                    print("Opción inválida!")
                    continue

                match opcion_modificar:
                    case 1:
                        telefono = input("Ingresa el nuevo número de teléfono: ")
                        agenda[contacto]["telefono"] = telefono
                    case 2:
                        email = input("Ingresa el nuevo email: ")
                        agenda[contacto]["email"] = email
                    case 3:
                        direccion = input("Ingresa la nueva direccion: ")
                        agenda[contacto]["direccion"] = direccion
                    case _:
                        print("Opción no válida!")
            else:
                print("No existe contacto a modificar")


        case 3:
            contacto = input("Ingresa el nombre del contacto que desea eliminar: ")
            if contacto in agenda:
                del agenda[contacto]
                print("El contacto se elimino correctamente: ")
            else:
                print("El contacto no existe")

        case 4:
            print(f"--- Lista de contactos ---\n")
            if agenda:
                for key, value in agenda.items():
                    print(f"""--- {key} ---
Telefono: {value['telefono']}
Email: {value['email']}
Dirección: {value['direccion']}
""")
            else:
                print("No hay contactos")

        case _:
            print("La opción no es válida!")
