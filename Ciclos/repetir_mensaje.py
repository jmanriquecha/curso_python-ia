print("Repetir mensaje")

mensaje = input("Ingresa el mensaje que desea repetir: ")

try:
    repeticiones = int(input("¿Cuántas veces quiere que se repita el mensaje: "))
except ValueError:
    print("Solo ingresa valores númericos")
    exit()

for _ in range(repeticiones):
    print(mensaje)