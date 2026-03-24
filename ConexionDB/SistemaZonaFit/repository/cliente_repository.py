
import mysql.connector

from database.conexion import Conexion
from models.cliente import Cliente


class ClienteRepository:

    def insertar(self, cliente):

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = "INSERT INTO clientes (nombre, apellido, membresia) VALUES(%s, %s, %s)"
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(sql, valores)
            conexion.commit()

            print(f"Cliente {cliente.nombre}, se guardo correctamente!")

        except mysql.connector.Error as error:
            print(f"Error: {error}")

        except Exception as e:
            print(f"Ocurrio un error: {e}")

        finally:
            if conexion.is_connected():
                cursor.close()
                Conexion.liberar_conexion(conexion)


    def editar(self, cliente):
        try:
            if self.buscar_id(cliente):
                return self.buscar_id(cliente)

        except mysql.connector.Error as error:
            print(f"Error: {error}")



    def actualizar(self, cliente):
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            campos = []
            valores = []

            if cliente.nombre:
                campos.append("nombre = %s")
                valores.append(cliente.nombre)

            if cliente.apellido:
                campos.append("apellido = %s")
                valores.append(cliente.apellido)

            if cliente.membresia:
                campos.append("membresia = %s")
                valores.append(cliente.membresia)

            # IMPORTANTE: unir campos correctamente
            sql_set = ", ".join(campos)

            sql = f"UPDATE clientes SET {sql_set} WHERE id = %s"

            # agregar el id al final
            valores.append(cliente.cliente_id)

            cursor.execute(sql, tuple(valores))
            conexion.commit()

            return cursor.rowcount

        except mysql.connector.Error as error:
            print(f"Error: {error}")

        finally:
            if conexion.is_connected():
                cursor.close()
                Conexion.liberar_conexion(conexion)


    def listar_todos(self):
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = "SELECT * FROM clientes"
            cursor.execute(sql)
            resultados = cursor.fetchall()

            clientes = [Cliente(cliente_id=r[0], nombre=r[1], apellido=r[2], membresia=r[3]) for r in resultados]

            return clientes

        except mysql.connector.Error as error:
            print(f"Error: {error}")

        finally:
            if conexion.is_connected():
                cursor.close()
                Conexion.liberar_conexion(conexion)


    def buscar_id(self, cliente):
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = "SELECT * FROM clientes WHERE id = %s"
            values = (cliente.cliente_id,)
            cursor.execute(sql, values)

            resultado = cursor.fetchone()

            if resultado is not None:
                return Cliente(cliente_id=resultado[0], nombre=resultado[1], apellido=resultado[2], membresia=resultado[3])
            else:
                print(f"No se encontro el cliente con id {cliente.cliente_id}")

        except mysql.connector.Error as error:
            print(f"Error: {error}")

        finally:
            if conexion.is_connected():
                cursor.close()
                Conexion.liberar_conexion(conexion)


    def eliminar(self, cliente):
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = "DELETE FROM clientes WHERE id = %s"
            values = (int(cliente.cliente_id),)
            cursor.execute(sql, values)
            conexion.commit()

            if cursor.rowcount > 0:
                print(f"Se elimino el cliente {cliente.cliente_id} correctamente")
            else:
                print("No se encontro el registro ó ya fue eliminado!")

        except mysql.connector.Error as error:
            print(f"Error: {error}")

        except Exception as e:
            print(f"Ocurrio un error: {e}")

        finally:
            if conexion.is_connected():
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == "__main__":
    cliente_repository = ClienteRepository()
    cliente_repository.eliminar(4)