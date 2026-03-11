print("Funciones recursivas")

def cuenta_regresiva(n):
    if n < 1:
        return 1

    if n == 1:
        print(n, end=" ")
        return n

    else:
        cuenta_regresiva(n - 1)
        print(n, end=" ")


cuenta_regresiva(10)
