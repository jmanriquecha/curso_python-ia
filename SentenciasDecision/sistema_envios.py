print("*** Sistema de envios ***")

# Determinar el costo de envio de un paquete segun el destino (Nacional, Internacional) y el peso del paquete

TARIFA_NACIONAL = 10 #1O pesos por kilo
TARIFA_INTERNACIONAL = 20 #20 pesos por kilo

destino = input("Ingrese el destino (Nacional/Internacional): ").lower()

try:
    peso_kilos = int(input("Ingrese el peso en kilos: "))
except ValueError:
    print("El valor del peso en kilos solo se permite números")
    exit()

if (destino != "nacional") and (destino != "internacional"):
    print("Destino no válido")
    exit()

if destino == "nacional":
    costo_envio = peso_kilos * TARIFA_NACIONAL
else:
    costo_envio = peso_kilos * TARIFA_INTERNACIONAL

msg = f"El costo del envio es: ${costo_envio}"
print(msg)