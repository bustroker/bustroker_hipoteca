from calculadora import Calculadora
from hipoteca import Hipoteca

class HipotecaVariable:
    def __init__(self, capital_prestado, meses, TIN_año_1, diferencial_interés_desde_año_2, euríbor_desde_año_2): # el TIN es el euríbor + diferencial
        self.nombre = "Variable"
        self.capital_prestado = capital_prestado
        self.meses = meses
        self.TIN_año_1 = TIN_año_1
        self.diferencial_interés_desde_año_2 = diferencial_interés_desde_año_2
        self.euríbor_desde_año_2 = euríbor_desde_año_2

    def hipoteca_año_1(self):
        return Hipoteca("Primer año", self.capital_prestado, self.meses, self.TIN_año_1)

    def hipoteca_desde_año_2(self, hipoteca_año_1):
        TIN_desde_año_2 = self.euríbor_desde_año_2 + self.diferencial_interés_desde_año_2
        return self.hipoteca_año_1().revisa_hipoteca_después_de_n_pagos(12, TIN_desde_año_2)

    def formato_chulo(self):
        hipoteca_año_1 = self.hipoteca_año_1()
        hipoteca_desde_año_2 = self.hipoteca_desde_año_2(hipoteca_año_1)
        return hipoteca_año_1.formato_chulo() + "\n" + hipoteca_desde_año_2.formato_chulo()
        

