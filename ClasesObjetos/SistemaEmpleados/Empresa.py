from SistemaEmpleados.Empleado import Empleado


class Empresa:

    def __init__(self, nombre):
        self._nombre = nombre
        self._empleados = []


    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self._empleados.append(empleado)

    def optener_numero_empleados_por_departamento(self, departamento):
        cuenta_empleados_departamento = 0
        for empleado in self._empleados:
            if empleado._departamento == departamento:
                cuenta_empleados_departamento += 1

        return cuenta_empleados_departamento

    def imprimir_empleados(self):
        print(f":::::::: Empleados de la empresa {self._nombre} :::::::::::")
        for empleado in self._empleados:
            print(f"-> ID: {empleado.get_id_empleado()} | Nombre: {empleado._nombre} Área: {empleado._departamento}")

        print("------------------------------")

