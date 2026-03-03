login = input("Desea continuar dentro del sistema? (Sí/No)").lower().strip()
msg = None

if not login == "si":
    msg = "Continuamos dentro del sistema..."
else:
    msg = "Saliendo del sistema..."

print(msg)