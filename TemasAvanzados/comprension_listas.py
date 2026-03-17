print("*** Comprensión de Listas ***")

# Numeros pares
# for i in range(6):
#     print(i)
#
# pares = [x for x in range(10) if x % 2 == 0]
# print(pares)

# Filtrar números pares
# Metodo tracicional

numeros = [0, 1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
numeros_pares = []
# for numero in numeros:
#     if numero % 2 == 0:
#         numeros_pares.append(numero)
#
# print(numeros_pares)

# Con compresion de listas
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)