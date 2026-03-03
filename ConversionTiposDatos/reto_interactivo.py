from random import randint

numero = input("Ingresa un número: ")

# Convertir str a entero
numero_int = int(numero)

# Convertir int a bool()
numero_bool = bool(numero_int)

print(f"""
Original: {numero}
Valor Entero: {numero_int}
Valor bool: {numero_bool}
""")

###

# Genera número aleatorio
aleatorio = randint(0,1)
# Convierte aleatorio en bool()
aleatorio_bool = bool(aleatorio)

print(f"""
Número Aleatorio: {aleatorio}
Valor booleano: {aleatorio_bool}
""")
