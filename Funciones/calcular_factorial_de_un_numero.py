print("Calcula el factorial de un número")


def fac_numero(numero):
    if numero == 0 or numero == 1:
        #print(f"Factorial de {numero} = 1")
        return 1
    else:
        factorial = numero * fac_numero(numero - 1)
        #print(f"factorial de {numero} = {factorial}")
        return factorial


if __name__ == "__main__":
    try:
        numero = int(input("Ingresa un número para allar su factorial: "))
    except ValueError:
        print("Ingresa un valor válido")

    if numero < 0:
        print("El factorial no esta definido para números negativos!")
    else:
        factorial = fac_numero(numero)
        print(f"Factorial de {numero}! = {factorial}")
