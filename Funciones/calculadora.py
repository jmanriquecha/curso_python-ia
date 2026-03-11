def sumar(n1, n2):
    return n1 + n2


def restar(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    if n2 == 0:
        return "No es posible dividir un número por cero"
    return n1 / n2

def mostrar_menu():
    menu = """
    ::::::::::::::::::::::::::::::::::::::::::::
    --- Calculadora ---
    ::::::::::::::::::::::::::::::::::::::::::::
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
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

        try:
            numero1 = float(input("Ingresa el valor 1: "))
        except ValueError:
            print("Ingresa un valor numérico")
            continue

        try:
            numero2 = float(input("Ingresa el valor 2: "))
            continue
        except ValueError:
            print("Ingresa un valor numérico")

        match opcion:
            case 0:
                print("Saliendo del sistema, hasta pronto!")
                break

            case 1:
                resultado = sumar(numero1, numero2)
                print(f"Resultado de la suma: {resultado:.2f}")

            case 2:
                resultado = restar(numero1, numero2)
                print(f"Resultado de la resta: {resultado:.2f}")

            case 3:
                resultado = multiplicar(numero1, numero2)
                print(f"Resultado de la multiplicación: {resultado:.2f}")

            case 4:
                resultado = dividir(numero1, numero2)
                print(f"Resultado de la división: {resultado:.2f}")

            case _:
                print("La opción seleccionada no es válida, por favor verifica e intenta de nuevo!")


if __name__ == "__main__":
    mostrar_menu()