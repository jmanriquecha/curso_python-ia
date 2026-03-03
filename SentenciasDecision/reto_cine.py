print('Sistema de Decisión (Escenario real: cine)')

es_cliente_vip = False
tiene_entrada = True
es_empleado = False

if es_empleado or (es_cliente_vip and not tiene_entrada):
    mensaje = "Entrada gratuita"
elif not es_cliente_vip and not es_empleado and tiene_entrada:
    mensaje = "Entrada permitida"
else:
    mensaje = "No puede entrar"

print(mensaje)