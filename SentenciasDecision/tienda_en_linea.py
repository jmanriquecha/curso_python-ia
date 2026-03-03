# Descuento

print(("*** Sistema de tienda en linea ***"))

monto_compra = float(input("Ingreda el monto de compra hoy? "))
es_miembro = input("Es miembro de la tienda? (Sí/No)").lower()

# Variables
descuento = 0
porcentaje_descuento = 0

#Si ha comprado más de 1000 y es miembro descuento del 10%
COMPRA_MINIMA_DESCUENTO = 1000

if monto_compra > COMPRA_MINIMA_DESCUENTO and es_miembro == "si":
    porcentaje_descuento = 10
    descuento = monto_compra * (porcentaje_descuento / 100)

# Sí solo es miembro descuento de 5%
elif es_miembro == "si":
    porcentaje_descuento = 5
    descuento = monto_compra * (porcentaje_descuento / 100)

# Sí no 0%
else:
    descuento = 0

precio_final_con_descuento = monto_compra - descuento

mensaje = f"""
#### Valor Compra ####
Precio sin descuento: {monto_compra}
Porcentaje descuento: {porcentaje_descuento}%
Descuento: {descuento}
-------------------------------------------
Precio final: {precio_final_con_descuento}"""

print(mensaje)