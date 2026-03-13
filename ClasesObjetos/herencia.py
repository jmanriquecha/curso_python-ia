class Animal:

    def comer(self):
        print('Como muchas veces')


    def dormir(self):
        print('Duermo muchas veces')


# herencia
class Perro(Animal):

    def comer(self):
        print("Me gusta mucho las croquetas y la carne")

    def hacer_sonidos(self):
        print("Hago waf waf!")


class Gato(Animal):
    def hacer_sonido(self):
        print('Hago miauuu!')


animal1 = Animal()
animal1.comer()

perro = Perro()
perro.comer()
perro.dormir()
perro.hacer_sonidos()


gato = Gato()
gato.dormir()
gato.hacer_sonido()