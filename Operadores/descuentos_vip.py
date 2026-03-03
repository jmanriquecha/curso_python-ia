# Una tienda de supermercados ofrece descuento especial a clientes que compren 10 ó mas articulos por día y ademas sean miembros de la tienda

print("*** Sistema de descuentos VIP ***")

nombre = input("Nombre del cliente: ")
cantidad_articulos = int(input("¿Cuántos articulos comprados hoy?: "))
es_miembro = bool(input(("Ingrese si es miembro de la tienda: '(0 = No, 1 = Sí)'")))

descuento_vip = (cantidad_articulos >= 10 and es_miembro == True)

print(f"""
El cliente {nombre} ¿tiene descuento? {descuento_vip}
""")