
def superheroe(nombre, *args, **kwargs):
    print(nombre, args, kwargs)
    print("### Superpoderes: ###\n")
    for superpoder in args:
        print(f"- {superpoder}")

    print("___ Más información ___\n")

    for key, value in kwargs.items():
        print(f"-> {key} : {value}")

superheroe("spiderma", "instinto arácnido", "telaraña", edad=25, empresa="marvel")
superheroe("vecino", personalidad="buena onda")
