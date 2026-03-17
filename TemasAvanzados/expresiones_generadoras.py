print("Expresiones Generadoras")

generador_cuadrados = (x**2 for x in range(10+1) if x % 2 == 0)


# Iterar generador
for valor in generador_cuadrados:
    print(valor)