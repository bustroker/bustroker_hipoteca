from calculadora import Calculadora

class Hipoteca:
    def __init__(self, capital_préstamo, meses, TIN): # el TIN es el euríbor + diferencial
        self.capital_prestado = capital_préstamo
        self.meses = meses # total de cuotas/meses a pagar
        self.interés_efectivo_mensual = TIN/1200 # tipo interés mensual efectivo. Divido por 12 y por 100 para convertir el porciento
        self.calculadora = Calculadora()

        self.cuota = self.calculadora.cuota(self.capital_prestado, self.interés_efectivo_mensual, self.meses)

    def deuda_después_de_n_pagos(self, n):
        return self.calculadora.deuda_después_de_n_pagos(self.cuota, self.interés_efectivo_mensual, self.meses, n)

    def revisa_hipoteca_después_de_n_pagos(self, n, nuevo_TIN):
        
        nuevo_capital = self.deuda_después_de_n_pagos(n)
        nuevos_meses = self.meses - n

        nueva_hipoteca = Hipoteca(nuevo_capital, nuevos_meses, nuevo_TIN)
        return nueva_hipoteca

    def pretty_format(self):
        result = "Capital prestado: " + str(self.capital_prestado) + "\nNro. meses: " + str(self.meses)  + "\nInterés efectivo mensual: " + str(self.interés_efectivo_mensual) + "\nCuota: " + str(self.cuota)
        return result