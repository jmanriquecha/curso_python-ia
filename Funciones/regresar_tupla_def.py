print("*** Regresar una tupla de valores desde una función ***")

# definir la función
def persona_mayusculas(nombre, apellido, edad):
    print("Esta función devuelve varios valores (Tupla)")
    return nombre.upper(), apellido.upper(), edad


nombre, apellido, edad = persona_mayusculas("Carlos", "Perez", 20)

print(f"Datos de la persona en MAYÚSCULAS. Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")