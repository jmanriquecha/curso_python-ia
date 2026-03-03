
play_list = []
print("Agrega canciones a tú play list")

try:
    numero_canciones = int(input("¿Cuantas canciones deseas agregar a la lista de reprodución? "))
except ValueError:
    print("Solo se pueden agregar números")
    exit()

## Iterar
for i in range(numero_canciones):
    cancion = input(f"Ingresa nombre de la canción #{i + 1}: ")
    play_list.append(cancion)

# Ordena
play_list.sort()

for cancion in play_list:
    print(cancion)