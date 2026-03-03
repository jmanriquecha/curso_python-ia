#Valor dentro de rango

print("*** Valor dentro de Rango ***")

MIN = -10
MAX = 5
"""
MIN = 0
MAX = 10
USER_NUMBER = -1

USER_NUMBER >= 0 

"""

# SOlisita datos al usuario
user_number = int(input(f"Ingrese un número: " ))

# dentro_de_rango = user_number >= MIN and user_number <= MAX
# Simplificando
dentro_de_rango = MIN <= user_number <= MAX

print(f"Valor dentro de rango? {dentro_de_rango}")