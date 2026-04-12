from repository.cliente_repository import ClienteRepository
from models.cliente import Cliente
from utils.helpers import normaliza_sin_espacios_title


class ClienteService:

    def __init__(self):
        self._repo = ClienteRepository()


    @property
    def repo(self):
        return self._repo


    def crear_cliente(self, nombre, apellido, membresia):
        nombre = normaliza_sin_espacios_title(nombre)
        apellido = normaliza_sin_espacios_title(apellido)

        cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
        self._repo.insertar(cliente)

        return cliente

    def editar_cliente(self, cliente_id):
        cliente = Cliente(cliente_id=cliente_id)
        return self.repo.editar(cliente)


    def actualizar_cliente(self, cliente_id, nombre, apellido, membresia):
        nombre = normaliza_sin_espacios_title(nombre)
        apellido = normaliza_sin_espacios_title(apellido)

        cliente = Cliente(cliente_id, nombre, apellido, membresia)
        self.repo.actualizar(cliente)

        return cliente


    def listar_clientes(self):
        return self.repo.listar_todos()


    def buscar_cliente_id(self, cliente_id):
        cliente = Cliente(cliente_id=cliente_id)
        return self.repo.buscar_id(cliente)


    def eliminar_cliente(self, cliente_id):
        cliente = Cliente(cliente_id=cliente_id)
        return self.repo.eliminar(cliente)