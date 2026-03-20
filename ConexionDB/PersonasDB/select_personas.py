import mysql.connector

from conexion_db.conexion import conecta_db

def consultar_personas():
    try:
        conexion = conecta_db()
        personas = conexion.cursor()
        personas.execute("SELECT * FROM personas")
        resultados = personas.fetchall()
        for persona in resultados:
            print(persona)

    except mysql.connector.Error as error:
        print(f'Error: {error}')

    finally:
        if conexion.is_connected():
            personas.close()
            conexion.close()
            print("Conexion cerrada")

if __name__ == '__main__':
    consultar_personas()

