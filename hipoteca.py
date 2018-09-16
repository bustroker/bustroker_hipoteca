from calculadora import Calculadora

class Hipoteca:
    def __init__(self, nombre, capital_prestado, meses, TIN): # el TIN es el euríbor + diferencial
        self.nombre = nombre
        self.capital_prestado = capital_prestado
        self.total_de_meses = meses # total de cuotas/meses a pagar
        self.TIN = TIN
        self.interés_efectivo_mensual = TIN/1200 # tipo interés mensual efectivo. Divido por 12 y por 100 para convertir el porciento

        self.es_hipoteca_revisada = False
        self.meses_reales = meses # si la hipoteca se revisa, estos serán los que realmente apliquen hasta la revisión
        
        self.calculadora = Calculadora()

        self.cuota = self.calculadora.cuota(self.capital_prestado, self.interés_efectivo_mensual, self.total_de_meses)

    def deuda_después_de_n_pagos(self, n):
        return self.calculadora.deuda_después_de_n_pagos(self.cuota, self.interés_efectivo_mensual, self.total_de_meses, n)

    def revisa_hipoteca_después_de_n_pagos(self, n, nuevo_TIN):

        self.es_hipoteca_revisada = True
        self.meses_reales = n

        nuevo_capital = self.deuda_después_de_n_pagos(n)
        nuevos_meses = self.total_de_meses - n

        nueva_hipoteca = Hipoteca(self.nombre, nuevo_capital, nuevos_meses, nuevo_TIN)
        return nueva_hipoteca

    def total_a_devolver(self):
        return self.cuota * self.meses_reales

    def formato_chulo(self):
        return "Capital prestado: " + str(self.capital_prestado) + "\nNro. meses: " + str(self.total_de_meses) + "\nNro. meses reales: " + str(self.meses_reales)  + "\nCuota: " + str(self.cuota) + "\nInterés efectivo mensual: " + str(self.interés_efectivo_mensual) + "\nTIN: " + str(self.TIN)