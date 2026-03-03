print("*** Sistema de administración de cuentas ***")

menu = """
Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir

Escoge una opción
"""

opcion = 0
mensaje = None

while opcion != 3:

    try:
        opcion = int(input(menu))
    except ValueError:
        print("Solo ingrese números")
        continue

    if opcion == 1:
        mensaje = "Creando cuenta..."
    elif opcion == 2:
        mensaje = "Eliminando cuenta..."
    elif opcion == 3:
        mensaje = "Saliendo del sistema..."
    else:
        mensaje = "La opción no es válida"


    print(mensaje)