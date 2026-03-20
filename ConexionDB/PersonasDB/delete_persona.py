import mysql.connector

from conexion_db.conexion import conecta_db

def elimiar_persona(id):
    try:
        conexion = conecta_db()
        personas = conexion.cursor()
        sql = "DELETE FROM personas WHERE id = %s"
        valores = (id,)

        personas.execute(sql, valores)
        conexion.commit()
        print(f"Persona con id {id} se elimino correctamente")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        if conexion.is_connected():
            personas.close()
            conexion.close()
            print("Conexión cerrada")


if __name__ == "__main__":
    elimiar_persona(1)