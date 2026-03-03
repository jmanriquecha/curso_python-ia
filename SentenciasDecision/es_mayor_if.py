nombre = input("Ingresa tú nombre: ").capitalize()
edad = int(input("Ingresa tú edad: "))

if edad >= 18:
    print(f"Hola {nombre} eres mayor de edad")
else:
    print(f"Hola {nombre} eres menor de edad")

es_mayor = "Sí" if edad >= 18 else "No"
print(f"¿Es mayor de edad? {es_mayor}")
