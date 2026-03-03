# Saber cuanto mide una cadena


nombre = "nombre de la persona"
tamanio_nombre = len(nombre)
primero = nombre[0]
ultimo = nombre[len(nombre) - 1]

print(f"La cadena '{nombre}' tiene {tamanio_nombre} carácteres")
print(primero, ultimo)

"""
Mayúsculas y minúsculas
"""

texto_mayuscula = "HOLA MUNDO"
convertir_texto_minuscula = texto_mayuscula.lower()
print(f"El texto \"{texto_mayuscula}\" se convirtio a minúscula \"{convertir_texto_minuscula}\"")


texto_minuscula = "hola mundo en minuscula"
convertir_texto_mayuscula = texto_minuscula.upper()
print(f"El texto \"{texto_minuscula}\" se convirtio a MAYÚSCULA \"{convertir_texto_mayuscula}\"")
