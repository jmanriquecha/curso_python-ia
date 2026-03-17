# split


cadena = "Hola-Mundo-con-Python"

# dvidir cadena por -

resultado = cadena.split("-")

print(resultado)

# función find para buscar

buscar = cadena.find("Mundo") # Devuelve el index donde inicia y si no devuelve -1
print(buscar)

# remplazar con replace

nueva_cadena = cadena.replace('Mundo', 'Amigo')
print(nueva_cadena)

## Convertir a mayusculas y minusculas
texto = "prueba para convertir en mayusculas y en minusculas, PROBANDO"
nuevo_texto = texto.title() # Primera letra despues de espacio en Mayuscula
print(nuevo_texto)


## Elimina espacios
texto1 = '     Hola Mundo!    '
print(texto1.strip()) # Elimina espacios en ambos lados
print(texto1.lstrip()) #Elimina espacios a la izquierda
print(texto1.rstrip()) #Elimina espacios a la derecha

menu = """              Usuario
        Nombre:
        Apellido:
        Edad:
Elige una opción"""


print(menu.strip())

# Funciones lambda

# Estructura lambda argumentos: expresion

numeros = range(0, 10+1)

cuadrado = lambda x: x**2

print(cuadrado(10))