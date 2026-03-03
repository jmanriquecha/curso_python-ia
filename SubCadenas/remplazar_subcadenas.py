# Remplazar sub cadenas

frase = "Hola Mundo! eres muy bonito Mundo"
sub_cadena = "a todos"
remplaza = frase.replace("Mundo", sub_cadena)

print(remplaza)

url = "www.dominio.com/nuevo%20usuario%20elegido.py"
normaliza_url = url.replace("%20", "-")
print(f"url original {url}")
print(normaliza_url.replace(".py", ""))

texto = "Hola Mundo"
resultado = texto[texto.find("M"):].replace("o", "O")
print(resultado)

print("hola"[-21:100])
