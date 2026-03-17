# Funciones lambda
from functools import reduce
from os.path import join

# estructura

# lambda argumentos: expresion

cuadrado = lambda x : x ** 2
print(cuadrado(3))

# Elevar número a una potencia
potencia = lambda base, potencia: base ** potencia
print(potencia(10,40))

suma = lambda x, y: x + y
print(suma(30,2))

print((lambda x: x**3)(3))


# Con map y lambda
# Creamos una lista de números

numeros = [0,10, 2, 3, 4, 5, 6]

# obtener el cuadrado de cada número con map y lambda

cuadrado_map_lambda = list(map(lambda x:x**2, numeros))
print(cuadrado_map_lambda)

# normalizar datos en Minuscula La Primera Letra

nombres = ["walTER", "CARLOS", "camila", "kaREN", "RuBiElA MarTINEZ"]
normalizar_nombres = list(map(lambda nombre: nombre.strip().upper(), nombres))
print(normalizar_nombres)

# Con filter y lambda
pares_lambda = list(filter(lambda numero: numero % 2 == 0, numeros))
print(f"Pares con filter y lambda {pares_lambda}")

# Impares
im_pares_lamda = list(filter(lambda numero: numero % 2 != 0, numeros))
print(f"Impares con filter y lambda {im_pares_lamda}")

# reduce y funciones lambda
total_suma = reduce(lambda numero1, numero2: numero1 + numero2, numeros)
print(f"Total con reduce y lambda: {total_suma}")
total_ = sum(numeros)
print(total_)

# encontrar el mayor
mayor_reduce = reduce(lambda numero1, numero2: numero1 if numero1 > numero2 else numero2, numeros)
print(f"Mayor con reduce y lambda {mayor_reduce}")


# sorted

ordenar_nombres = sorted(nombres, reverse=True)
print(ordenar_nombres)

personas = [
    {"nombre": "Juan", "apellido": "Rodrigez", "edad": 20},
    {"nombre": "Karen", "apellido": "CASTRO", "edad": 18},
    {"nombre": "Alejandro", "apellido": "Arguello", "edad": 30},
    {"nombre": "Zenaida", "apellido": "Zamora", "edad": 28},
    {"nombre": "Beronica", "apellido": "Gutierrez", "edad": 17}
]

ordenar_personas = sorted(personas, key=lambda x: (x['nombre'], x['edad']))
print(ordenar_personas)
