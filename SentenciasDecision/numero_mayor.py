print("*** Verifica cual es el número mayor ***")

numero1 = int(input("Ingrese un  número: "))
numero2 = int(input("Ingrese un número: "))

if numero1 > numero2:
    mayor = numero1
else:
    mayor = numero2

msg = ""

if numero1 == numero2:
    msg = f"Los números son iguales"
else:
    msg = f"El número {mayor} es el mayor"

print(msg)