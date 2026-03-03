frutas = ["Pera", "Manzana", "Tomate"]

for i in range(len(frutas)):
    print(frutas[i])

# mofificar indece
frutas[0] = "Ciruela"
print(frutas[0])

# agregar valor
frutas.append("Curuba")

# eliminar elemento

del frutas[2]

print(frutas)

# Iterar lista
for item in frutas:
    print(item)


# Lista heterogenea

heterogenea = ["Hola", True, 20, 20.66]

for item in heterogenea:
    print(item)