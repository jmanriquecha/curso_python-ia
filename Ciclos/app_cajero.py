print("Bienvenido al cajero automatico")

saldo = 1000
salir = False
menu = """
Menú cajero
    1. Depositar
    2. Consultar saldo
    3. Retirar
    0. Salir
    
    Escoge una opción: """
mensaje = None
solo_numeros = "Solo se permiten ingresar números"

while not salir:
    try:
        option = int(input(menu))
    except ValueError:
        print(solo_numeros)
        continue

    if option == 0:
        mensaje = "Saliendo del sistema. Hasta pronto..."
        salir = True

    elif option == 1:
        try:
            deposito = float(input("Ingrese el valor que desea depositar: $"))
        except ValueError:
            print(solo_numeros)
            continue

        if deposito > 0:
            saldo += deposito
            mensaje = f"Su nuevo saldo es ${saldo:.2f}"
        else:
            mensaje = "El deposito no es válido"

    elif option == 2:
        mensaje = f"Su saldo actual es ${saldo:.2f}"

    elif option == 3:
        try:
            retirar = float(input("Ingrese el valor a retirar: $"))
        except ValueError:
            print(solo_numeros)
            continue

        # Validamos que tenga saldo suficiente en la cuenta
        if retirar <= saldo:
            saldo -= retirar
            mensaje = f"Retiro completado: Nuevo Saldo ${saldo:.2f}"
        else:
            mensaje = f"No cuentas con saldo suficientes: Tú saldo actual: {saldo:.2f}"

    else:
        mensaje = "La opción no es válida"

    print(mensaje)