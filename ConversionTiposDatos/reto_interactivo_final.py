from random import randint

numero = int(input("Ingresa un número: "))
aleatorio = randint(0,1)

# convertir números a bool

numero_bool = bool(numero)
aleatorio_bool = bool(aleatorio)

resultado =f"""
Número ingresado {numero}
Bool del número ingresado: {numero_bool}
Número aleatorio: {aleatorio}
Bool del número aleatorio: {aleatorio_bool}
"""

print(resultado)
