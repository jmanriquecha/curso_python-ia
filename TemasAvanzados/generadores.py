print("Generadores en Python")

def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1


# creamos un generador
var_generador = generador(20)


# Iteramos el generador
for valor in var_generador:
    print(valor)
