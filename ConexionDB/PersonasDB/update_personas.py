import mysql.connector

from conexion_db.conexion import conecta_db


def actualizar_personas(id, nombre=None, apellido=None, edad=None):
    try:
        conexion =  conecta_db()
        personas = conexion.cursor()

        sql = "UPDATE personas SET nombre = %s, apellido = %s, edad = %s WHERE id = %s"
        valores = (nombre, apellido, edad, id)

        personas.execute(sql, valores)
        conexion.commit()

        print("Se actualizó el registro")

    except mysql.connector.Error as error:
        print(f'Error: {error}')

    except Exception as e:
        print(f"Ocurrio un error: {e}")

    finally:
        if conexion.is_connected():
            personas.close()
            conexion.close()
            print("Conexión cerrada")


if __name__ == "__main__":

    actualizar_personas(2, nombre="Excelino", apellido="Garzon", edad=52)
