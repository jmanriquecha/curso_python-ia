class Tarea:

    def __init__(self, tarea_id=None, titulo=None, descripcion=None, finished_at=None, created_at=None, updated_at=None):
        self.tarea_id = tarea_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.finished_at = finished_at
        self.created_at = created_at
        self.updated_at = updated_at


    def __str__(self):
        return f"{self.tarea_id, self.titulo, self.descripcion, self.finished_at, self.created_at, self.updated_at}"
