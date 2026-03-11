print("Usando kwargs para imprimir información")

def imprimir_info(**kwargs):
    print("valores recibidos")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

imprimir_info(nombre="Bernardo", apellido="Triana", edad=20)