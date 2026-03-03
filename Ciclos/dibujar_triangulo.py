print("*** Dibuja triangulo ***")

try:
    altura = int(input("Tamaño del triangulo: "))
except ValueError:
    print("Solo ingresa números")
    exit()


"""
for i in range(1, altura + 1):
    espacios = altura - i
    estrellas = 2 * i - 1

    print(" " * espacios + "*" * estrellas)
"""

for fila in range(1, altura + 1):
    espacios = " " * (altura - fila) #Cantidad de espacios en blanco
    caracter = "*" * (2 * fila - 1) #Cantidad de caracteres para la fila actual
    print(f"{espacios} {caracter}") # Imprime espacios y asteriscos
