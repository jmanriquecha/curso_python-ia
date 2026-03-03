print("*** Sistema de autenticacion ***")

USER = "admin"
PASS = "1234pass"

# solicita datos al usuario

nombre_usuario = input("Ingresa el usuario: ")
pass_usuario = input("Ingresa la contraseña: ")

# valida login
if nombre_usuario == USER and pass_usuario == PASS:
    msg = f"Hola, {nombre_usuario} bienvenido de nuevo..."
elif nombre_usuario != USER and pass_usuario == PASS:
    msg = "Usuario inválido!"
elif pass_usuario != PASS and nombre_usuario == USER:
    msg = "Contraseña inválida!"
else:
    msg = "Usuario y contraseña inválidos!"

print(msg)