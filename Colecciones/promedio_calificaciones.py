print("Pormedio de calificaciones")

calificaciones_list = []


try:
    cantidad_calificaciones = int(input("Ingresa la cantidad de calificaciones: "))
except ValueError:
    print("Ingresa solo números")
    exit()
# Solicita al usuario ingresar las notas

for i in range(cantidad_calificaciones):
    while True:
        try:
            calificaion = float(input(f"Ingresa la calificación {i + 1}: "))
            break
        except ValueError:
            print("Ingresa solo números")

    calificaciones_list.append(calificaion)

# Sumatoria de calificaiones
suma_notas = sum(calificaciones_list)

# Obtine el promedio de notas
promedio = suma_notas / cantidad_calificaciones

print(f"Promedio de calificación es {promedio:.2f}")