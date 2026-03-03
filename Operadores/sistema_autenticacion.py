print("*** SISTEMA DE AUTENTICACIÓN ***")

PASSWORD = "1234"
USER = "jmanrique"

# Autenticación
user_name = input("Ingrese nombre de Usuario: ")
user_pass = input("Ingrese la contraseña: ")

valida_session = (user_name == USER
                  and user_pass == PASSWORD)

print(valida_session)