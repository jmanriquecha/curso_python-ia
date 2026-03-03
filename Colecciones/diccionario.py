print(" Trabajando con diccionarrios")

persona = {
    "nombre": "Jorge",
    "edad": 20,
    "ciudad": "Bogotá",
    "email": "jorge@mail.com"
}

# imprimir diccionario
print(persona)

# Acceder a la información

print(persona["nombre"])

# Forma segura
print(persona.get("email", "El mail no existe"))

# Iterar diccionario
for key, value in persona.items():
    print(f"{value}  -  {key}")