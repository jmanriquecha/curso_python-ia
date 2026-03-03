# Subcadenas
frase = "Hola mundo!"
sub_cadena = frase[0:4]

print(sub_cadena)

sub_mundo = frase[5:]
print(sub_mundo)

# subcadenas

email = "georgemanc.28@gmail.com"
email_arroba = email.index("@")
print(email_arroba)

nombre_usuario = email[:email_arroba]
print(nombre_usuario)

dominio = email[email_arroba:]
print(dominio)


"""
Buscar subcadenas en una cadena con find()
"""

cadena = "Hola Mundo!"
sub_cadena1 = "Mundo"
buscar_sub_cadena = cadena.find(sub_cadena1[2:])
print(buscar_sub_cadena)