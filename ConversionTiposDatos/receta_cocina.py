nombre_receta = input("Ingrese el nombre de la receta de cocina: ")
ingredientes = input("Ingrese los ingredientes: ")
tiempo_preparacion = int(input("¿Cuanto es el tiempo de preparación en minutos: "))
dificultad = input("Dificultad ('Facil, Media, Alta': ")

imprimir_reseta = f"""
MI RECETA DE COCINA

Nombre receta: {nombre_receta}
Ingredientes: {ingredientes}
Tiempo: {tiempo_preparacion} minutos
Dificultad: {dificultad}
"""

print(imprimir_reseta)