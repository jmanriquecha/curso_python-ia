class Aritmetica:
    contador = 0

    def __init__(self, operando1, operando2):
        self._operando1 = float(operando1)
        self._operando2 = float(operando2)

        self.contador += 1

    def get_operando1(self):
        return self._operando1

    def set_operando1(self, operando1):
        self._operando1 = operando1

    def get_operando2(self):
        return self._operando2

    def set_operando2(self, operando2):
        self._operando2 = operando2

    def sumar(self):
        return self._operando1 + self._operando2

    def restar(self):
        return self._operando1 - self._operando2

    def multiplicar(self):
        return self._operando1 * self._operando2

    def dividir(self):
        if self._operando2 == 0:
            return None
        return self._operando1 / self._operando2


def mostrar_resultado(obj):
    division = obj.dividir()
    if  division is None:
        division_str = f"No es posible dividir por cero"
    else:
        division_str = f"{division:.2f}"

    resultado = f"""
    Suma: {obj.sumar():.2f}
    Resta: {obj.restar():.2f}
    Multiplicación: {obj.multiplicar():.2f}
    División: {division_str}"""
    print(resultado)

valor1 = Aritmetica(10, 30)
mostrar_resultado(valor1)

valor2 = Aritmetica(15.5, 0)
valor2.set_operando2(0)
mostrar_resultado(valor2)
