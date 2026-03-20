import mysql.connector

from conexion_db.conexion import conecta_db

def insertar_registro(nombre, apellido, edad):
    try:
        conexion = conecta_db()
        personas = conexion.cursor()
        sql = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"
        valores = (nombre, apellido, edad)
        personas.execute(sql, valores)
        conexion.commit()
        print("Nuevo registro agregado correctamente")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        if conexion.is_connected():
            # Cerrar conexion
            personas.close()
            conexion.close()
            print("Conexión cerrada")

if __name__ == '__main__':
    nombre = input("Ingresa el nombre: ")
    apellido = input('Ingresa el apellido: ')
    edad = int(input('Ingresa la edad: '))

    insertar_registro(nombre, apellido, edad)