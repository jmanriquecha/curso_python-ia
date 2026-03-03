print("Valida Contraseña")

salir = False

while not salir:

    password = input("Ingresa la contraseña, minimo debe tener 6 caracteres: ")

    if len(password) >= 6:
        print(f"Contraseña creada correctamente: {password}")
        salir = True
    else:
        print(f"La contraseña no es válida: ")
