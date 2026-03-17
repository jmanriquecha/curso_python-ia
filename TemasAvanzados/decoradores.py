print("Decoradores en Python")

def decorador(fuction):

    def wrapper():
        print("antes de ejecutar el decorador")
        fuction()
        print("Despues de ejecutar el decorador")
    return wrapper


@decorador
def saludar():
    print("Hola mundo desde un decorador")

saludar()