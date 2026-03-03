from random import randint

print("Juego de adivinar el número secreto")

INTENTOS_PERMITIDOS = 10
salir = False
intentos = 1
numero_secreto = randint(1,50)
mensaje = None


while not salir:
    try:
        numero_usuario = int(input("Adivina el número secreto: "))
    except ValueError:
        print("Solo debe ingresar números ")
        continue
    if intentos < INTENTOS_PERMITIDOS:

        if numero_usuario == numero_secreto:
            mensaje = f"¡Felicidades Adivinaste! en {intentos}, el número secreto es {numero_secreto}"
            salir = True

        elif numero_usuario > numero_secreto:
            mensaje = "¡Estuviste cerca, el número secreto es menor!"
            intentos += 1
        else:
            mensaje = "¡Estuviste cerca, el número secreto es mayor!"
            intentos += 1
    else:
        mensaje = f"Lo siento (: agotaste el número de intentos permitidos: {INTENTOS_PERMITIDOS} \n Finalizando juego..."
        salir = True

    print(mensaje)