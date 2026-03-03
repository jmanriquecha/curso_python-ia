
cadena = input("Ingresa un texto para contar cuantas vocales contiene: ")
vocales = "aeiouáéíóú"
contador_vocales = 0

for i in range(len(cadena)):
    if cadena[i].lower() in vocales:
        contador_vocales += 1

print(f"Vocales encontradas: {contador_vocales}")