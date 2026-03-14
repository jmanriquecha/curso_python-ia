from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

if __name__ == "__main__":

    #Creamos ordenes
    raton = Raton("HP", "USB")
    raton1 = Raton('TRUST', 'USB')
    raton2 = Raton('LG', 'Bluetooth')
    teclado = Teclado("Genius", "WIFI")
    teclado1 = Teclado("Trush", "BLUETOOTH")
    monitor = Monitor('LG', '55')
    monitor1 = Monitor('SAMSUNG', '80')

    # Agrega commputadoras
    computadora = Computadora('HP', monitor, teclado, raton)
    computadora.monitor = monitor1
    computadora.raton = raton2

    computadora1 = Computadora('COMPAQ', monitor, teclado1, raton)

    # Generar ordenes
    orden1 = Orden([computadora])
    orden1.agregar_computadora(computadora1)
    print(orden1)
    print(f'Total Ordenes: {Orden.contador_ordenes()}')

