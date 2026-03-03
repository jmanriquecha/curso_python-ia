print("Convinacion de listas con tuplas")

# Definir una lista que almacena tuplas con productos
productos = [
    ("P001", "Camisa", 20.55),
    ("P002", "Pantalon", 50.01),
    ("P003", "Zapatos", 88.9)
]

precio_total = 0

# Recorrer
for tupla in productos:
    codigo, producto, precio = tupla
    precio_total += precio
    print(f"Codigo: {codigo}, Producto: {producto}, Precio: {precio:.2f}")

print(f"\nEl precio total es: {precio_total}")