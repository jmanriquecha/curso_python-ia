# genera Id unico
from random import randint

print("*********** Sistema Generador de ID Único ***********")

nombre = input("Ingresa nombre: ")
apellido = input(("Ingresa apellido: "))
fecha_nacido = input("Ingresa año de nacimiento ('YYYY'): ")

# nombre solo las dos primeras letras y convertirlas en MAYÚSCULAS
nombre_id = nombre[:2].upper()

# apellido solo las dos primeras letras y convertirlas en MAYÚSCULAS

apellido_id = apellido[:2].upper()

# fecha_nacido tomar solo los 2 últimos digitos
fecha_nacido_id = fecha_nacido[2:]

# generar numero aleatorio de 4 digitos con la funcion randint
numero_aleatorio = randint(1000,9999)

# Genera id
id_unico = f"{nombre_id}{apellido_id}{fecha_nacido_id}{numero_aleatorio}"

print(f"""
Hola, {nombre}
    Tú nuevo id generado por el sistema es: {id_unico}
    Felicitaciones.
""")