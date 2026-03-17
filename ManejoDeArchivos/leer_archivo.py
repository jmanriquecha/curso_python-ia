print('Leer archivos desde python')

nombre_archivo = 'mi_archivo.txt'

# Leyendo lineas
try:
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea.strip())
except Exception as e:
    print(f'Error: {e}')

# Leyendo el contenido con read()
try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except Exception as e:
    print(f'Error: {e}')