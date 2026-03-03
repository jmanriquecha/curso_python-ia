print("*** Sistema de Calificaciones ***")

try:
    calificacion = float(input("Ingresa la nota obtenida entre (0 y 10): "))
except ValueError:
    print("Ingrese solo números")
    exit()

if calificacion >= 9 and calificacion <= 10:
    letra = "A"
elif calificacion >= 8 and calificacion < 9:
    letra =  "B"
elif calificacion >= 7 and calificacion < 8:
    letra = "C"
elif calificacion >= 6 and calificacion < 7:
    letra = "D"
elif calificacion >= 0 and calificacion < 6:
    letra = "F"
else:
    print("Valor desconocido")
    exit()

print(f"La calficación obtenida es: {letra}")