from src.repository.tarea_repository import TareaRepository
from src.model.tarea import Tarea


class TareaService:

    TAREA_REPOSITORY = TareaRepository()

    @classmethod
    def crear(cls, titulo, descripcion):
        if titulo is not None and titulo.strip() == "":
            raise ValueError("El título no puede estar vacio")

        if descripcion is not None and descripcion.strip() == "":
            raise ValueError("La descripción no puede estar vacía")

        titulo = cls.normalizar_datos(titulo)
        descripcion = cls.normalizar_datos(descripcion)

        return cls.TAREA_REPOSITORY.insertar(Tarea(titulo=titulo, descripcion=descripcion))


    @classmethod
    def actualizar(cls, tarea_id, titulo, descripcion):
        if titulo is not None and titulo.strip() == "":
            raise ValueError("El título no puede estar vacio")

        if descripcion is not None and descripcion.strip() == "":
            raise ValueError("La descripción no puede estar vacía")

        titulo = cls.normalizar_datos(titulo)
        descripcion = cls.normalizar_datos(descripcion)

        return cls.TAREA_REPOSITORY.actualizar(Tarea(tarea_id=tarea_id, titulo=titulo, descripcion=descripcion))


    @classmethod
    def finalizar_tarea(cls, tarea_id):
        return cls.TAREA_REPOSITORY.finalizar(Tarea(tarea_id=tarea_id))

    @classmethod
    def tareas_finalizadas(cls):
        return cls.TAREA_REPOSITORY.tareas_finalizadas()


    @classmethod
    def tareas_activas(cls):
        return cls.TAREA_REPOSITORY.tareas_activas()


    @classmethod
    def normalizar_datos(cls, valor):
        return valor.strip().title()

if __name__ == "__main__":
#     tareas = TareaService.REPO.tareas_finalizadas()
#     for activa in tareas:
#         print(activa)
    tareas = TareaService.crear("Prueba", "Descripcion")
