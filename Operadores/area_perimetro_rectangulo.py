print("*** Sistema para calcular área y perimetro de un Rectangulo ***")

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

# Calculos

area = base * altura
perimetro = 2 * (base + altura)

resultado = f"""
Área: {area:.2f}
Perímetro: {perimetro:.2f}
"""

print(resultado, 2 ** 2)