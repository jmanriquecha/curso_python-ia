print("Calculadora en Python")

# permite operar 2 números

salir = False
solo_numeros = "Solo se permiten números"
numero1 = numero2 = 0
menu = """
Operaciones que puede realizar
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    0. Salir
    
Escoge una opción: 
"""

while not salir:
    try:
        option = int(input(menu))
    except ValueError:
        print(solo_numeros)
        continue


    if option == 0:
        msg_resultado = "Saliendo de la calculadora..."
        salir = True

    if 1 <= option <= 4:
        try:
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print(solo_numeros)
            continue

    if option == 1:
        resultado = numero1 + numero2
        msg_resultado = f"La suma de {numero1:.2f}+{numero2:.2f} es: {resultado:.2f}"

    elif option == 2:
        resultado = numero1 - numero2
        msg_resultado = f"La resta de {numero1:.2f}-{numero2:.2f} es: {resultado:.2f}"

    elif option == 3:
        resultado = numero1 * numero2
        msg_resultado = f"La multiplicación de {numero1:.2f}X{numero2:.2f} es: {resultado:.2f}"

    elif option == 4:
        if numero2 == 0:
            msg_resultado = f"No es posible divider por Cero (0)"
        else:
            resultado = numero1 / numero2
            msg_resultado = f"La división de {numero1:.2f}/{numero2:.2f} es: {resultado:.2f}"

    else:
        msg_resultado = "La opción seleccionada no es válida!"

    print(msg_resultado)


