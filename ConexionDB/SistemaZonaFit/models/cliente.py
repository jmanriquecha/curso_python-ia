class Cliente:

    def __init__(self, cliente_id = None, nombre = None, apellido = None, membresia = None):
        self._cliente_id = cliente_id
        self._nombre = nombre
        self._apellido = apellido
        self._membresia = membresia


    @property
    def cliente_id(self):
        return self._cliente_id


    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self._cliente_id = cliente_id


    @property
    def nombre(self):
        return self._nombre


    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def apellido(self):
        return self._apellido


    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido


    @property
    def membresia(self):
        return self._membresia


    @membresia.setter
    def membresia(self, membresia):
        self._membresia = membresia


    def __str__(self):
        return f"-> {self.cliente_id}, {self.nombre}, {self.apellido}, {self.membresia}"