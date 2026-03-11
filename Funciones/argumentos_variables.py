print("*** Argumentos variables ***")

def superherohe(superheroe, nombre, *args):
    print(f"{superheroe.capitalize()} - {nombre.capitalize()} - {args}")
    # Iteramos super poderes
    for superpoder in args:
        print(f"Superpoder - {superpoder.capitalize()}")


# LLamar funcion
superherohe("Spiderman", "peter parker", "arácnido", "Telaraña", "volar")

# Roy barreras consula
# Senado Pacto Historico