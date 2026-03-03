a, b, c = 10, 3, 2
resultado = a + b * c ** 2

resultado += 5
resultado *= 2

es_valido = resultado > 30 and not resultado == 50

print(resultado)

print(es_valido)