print('Excepciones en Python')

# edad = int(input("Ingrese la edad: "))
#
# if edad < 0:
#     raise ValueError('La edad no puede ser menor que cero')

def division(n1, n2):
    try:
        resultado = n1 / n2
        print(resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")


division(10,5)
division(12, 0)
division(20,10)