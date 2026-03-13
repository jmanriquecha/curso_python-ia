from SistemaEmpleados.Empleado import Empleado
from SistemaEmpleados.Empresa import Empresa

if __name__ == "__main__":
    empresa1 = Empresa('Mi empresa SAS ')
    empresa1.contratar_empleado('camilo', 'prensa')
    empresa1.contratar_empleado('Juan', 'prensa')

    #Imprimir empleados de la empresa
    empresa1.imprimir_empleados()

    """buscar_numero_empleados = empresa1.optener_numero_empleados_por_departamento('prensa')
    print(buscar_numero_empleados)"""
    print(f"Total empleados: {Empleado.obtener_total_empleados()}")

    ## Agregar empleados a otra empresa
    empresa2 = Empresa('JERAS SAS')
    empresa2.contratar_empleado('Joaquin', 'Ventas')
    empresa2.imprimir_empleados()
    print(f"Total empleados: {Empleado.obtener_total_empleados()}")

