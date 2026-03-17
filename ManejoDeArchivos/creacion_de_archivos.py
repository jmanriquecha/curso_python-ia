print("Crear Archivo con Python")

nombre_archivo = 'mi_archivo.txt'

# Abrir archivo en modo escritura ('w')

# archivo = open(nombre_archivo, 'w')
# archivo.write("Hola estoy agregando texto desde python\n")
# archivo.write("Esta es una nueva linea agregada desde python\n")
# archivo.write("Esta es la tercera linea\n")
# archivo.write("Esta es la cuarta linea agregada")
# archivo.close()

# Forma más profesional con with
with open(nombre_archivo, 'w') as archivo:
    archivo.write("primera linea de codigo agregada\n")
    archivo.write("continuando con la generación de archivos")


print(f'Se creo el archivo: {nombre_archivo}')