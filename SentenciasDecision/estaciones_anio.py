try:
    mes = int(input("Ingresa el número de un mes: (1 a 12) "))
except ValueError:
    print("Debes ingresar solo números")
    exit()

mes_valido = 1 <= mes <= 12

if not mes_valido:
    print("El mes ingresado no es vádido")
    exit()
if mes in(1,2,12):
    estacion = "Invierno"
elif mes in(3,4,5):
    estacion = "Primavera"
elif mes in(6,7,8):
    estacion = "Verano"
elif mes in(9,10,11):
    estacion = "Otoño"

print(f"La estación del año es {estacion}")

