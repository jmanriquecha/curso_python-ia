def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b


operaciones = {
    1: ("Sumar", sumar),
    2: ("Restar", restar),
    3: ("Multiplicar", multiplicar),
    4: ("Dividir", dividir)
}

print(operaciones[1][1])


def mostrar_menu():
    while True:
        print("\n--- Calculadora ---")

        for clave, valor in operaciones.items():
            print(f"{clave}. {valor[0]}")
        print("0. Salir")

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Ingresa un número válido")
            continue

        if opcion == 0:
            print("Saliendo...")
            break

        if opcion not in operaciones:
            print("Opción inválida")
            continue

        try:
            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))
        except ValueError:
            print("Debes ingresar números")
            continue

        funcion = operaciones[opcion][1]
        resultado = funcion(n1, n2)

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    mostrar_menu()