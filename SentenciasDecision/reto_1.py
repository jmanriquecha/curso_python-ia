print("*** Reto 1 – Sistema de Decisión (mundo real con bool y lógica) ***")

es_usuario = True
es_admin = False
tiene_suscripcion = True

if es_admin:
    mensaje = "Acceso total"
elif not es_admin == True and es_usuario and tiene_suscripcion:
    mensaje = "Acceso limitado"
else:
    mensaje =  "Acceso denegado"

print(mensaje)