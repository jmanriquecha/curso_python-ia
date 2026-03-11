print("*** Función con argumentos por nombre ***")

if __name__ == "__main__":
    def crear_persona(nombre="", apellido="", edad=0):
        print(f"Persona - nombre: {nombre}, apellido: {apellido}, edad: {edad}")


    crear_persona(apellido="Manrique")