print("Función es par")

def es_par(numero):
    return f"{numero} Es par" if numero % 2 == 0 else f"{numero} Es impar"


if __name__ == "__main__":
    resultado = es_par(28)
    print(resultado)
