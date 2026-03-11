print("Suma con argumentos variables")

def sumar(*args):
    total = 0
    for numero in args:
        total += numero

    print(f"Total suma: {total}")


sumar(10,20,30)