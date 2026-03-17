# función zip


nombres = ['Karen', 'Jaime', 'Rodrigo']
edades = [20, 30, 15]

resultado = zip(nombres, edades)

#print(list(resultado))

# Desempaquetando

nombres1, edades1 = zip(*resultado)
print(nombres1)
print(edades1)