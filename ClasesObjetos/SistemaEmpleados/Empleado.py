class Empleado:

    _contador_empleados = 0

    def __init__(self, nombre, departamento):
        Empleado._contador_empleados += 1
        self.__id_empleado = Empleado._contador_empleados
        self._nombre = nombre
        self._departamento = departamento


    @classmethod
    def obtener_total_empleados(cls):
        return cls._contador_empleados

    def get_id_empleado(self):
        return self.__id_empleado
