# Sistema generador de emails

print("*** Sistema generador de Emails ***")

nombre = input("Ingresa tú nombre: ")
apellido = input("Ingresa tú apellido: ")

# Convertir a minusculas
nombre_min = nombre.lower()
apellido_min = apellido.lower()

# @
arroba = "@"

# dominio
dominio = "empresa.com"

# email generado
email = f"{nombre_min}.{apellido_min}{arroba}{dominio}"

print(f"""
Hola {nombre.capitalize()},
    Tú email generado por el sistema es: {email}
    Cordialmente,
    Equipo de Soporte
""")