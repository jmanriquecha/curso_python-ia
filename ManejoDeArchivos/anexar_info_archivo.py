print('Anexar información a un archivo que ya existe')

nombre_archivo = 'mi_archivo.txt'

try:
    with open(nombre_archivo, 'a') as archivo:
        archivo.write('Nueva Linea de texto\n')
    print('se agrego texto')
except Exception as e:
    print(f'Error: {e}')


# Leer archivo

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)

except Exception as e:
    print(f'Error {e}')