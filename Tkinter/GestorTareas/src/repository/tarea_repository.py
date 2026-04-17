from datetime import datetime

from src.database.conexion import Conexion
from src.model.tarea import Tarea


class TareaRepository:

    def __init__(self):
        self.conexion = Conexion()


    def insertar(self, tarea):
        try:
            conexion = self.conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = "INSERT INTO tareas (titulo, descripcion, created_at) VALUES(%s, %s, %s)"
            values = (tarea.titulo, tarea.descripcion, datetime.now())
            cursor.execute(sql, values)
            conexion.commit()
        except Exception as e:
            raise ValueError(f"Error: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                Conexion.liberar_conexion(conexion)


    def actualizar(self, tarea):
        try:
            conexion = self.conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = "UPDATE tareas SET titulo=%s, descripcion=%s, updated_at=%s WHERE id = %s"
            values = (tarea.titulo, tarea.descripcion,  datetime.now(), tarea.tarea_id)
            cursor.execute(sql, values)
            conexion.commit()

            return cursor.rowcount
        except Exception as e:
            raise ValueError(f"Error: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                Conexion.liberar_conexion(conexion)


    def finalizar(self, tarea):
        try:
            conexion = self.conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = "UPDATE tareas SET finished_at=%s WHERE id = %s"
            values = (datetime.now(), tarea.tarea_id)
            cursor.execute(sql, values)
            conexion.commit()

            return cursor.rowcount
        except Exception as e:
            raise ValueError(f"Error: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                Conexion.liberar_conexion(conexion)


    def tareas_finalizadas(self):
        try:
            conexion = self.conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = "SELECT * FROM tareas WHERE finished_at IS NOT NULL "
            cursor.execute(sql)
            resultados = cursor.fetchall()

            tareas = [self.mapear_tarea(resultado) for resultado in resultados]

            return tareas
        except Exception as e:
            raise ValueError(f"Error: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                Conexion.liberar_conexion(conexion)


    def tareas_activas(self):
        try:
            conexion = self.conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = "SELECT * FROM tareas WHERE finished_at IS NULL"
            cursor.execute(sql)
            resultados = cursor.fetchall()

            tareas = [self.mapear_tarea(resultado)
                      for resultado in resultados]

            return tareas
        except Exception as e:
            raise ValueError(f"Error: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                Conexion.liberar_conexion(conexion)


    def mapear_tarea(self, resultado):
        return Tarea(
            tarea_id=resultado[0],
            titulo=resultado[1],
            descripcion=resultado[2],
            finished_at=resultado[3],
            created_at=resultado[4],
            updated_at=resultado[5])


if __name__ == "__main__":
#     # Insertar tarea
#     # tarea = Tarea(titulo="💡Tarea 12", descripcion="Organizar el archivo")
#     # tarea_repository = TareaRepository()
#     # tarea_repository.insertar(tarea)
#
#     # Actualizar tarea
#     # tarea = Tarea(tarea_id=11, titulo="Tarea 8", descripcion="Muy bien como se modifica todo el campo desde python con el gestor de tareas")
#     # tarea_repository = TareaRepository()
#     # tarea_repository.actualizar(tarea)
#
#     # Completar tarea
#     # tarea = Tarea(tarea_id=11)
#     # repo = TareaRepository().finalizar(tarea)
#
#     # Listar tareas completadas
#     # print("Tareas finalizadas")
#     # repo = TareaRepository()
#     # for tarea in repo.tareas_finalizadas():
#     #     print(tarea)
#
#     # Listar tareas activas
    repo = TareaRepository()
    print("Tareas activas")
    for tarea in repo.tareas_activas():
        print(tarea)