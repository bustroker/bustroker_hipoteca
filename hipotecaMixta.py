from calculadora import Calculadora
from hipoteca import Hipoteca

# n meses a TIN fijo y luego con diferencial + euríbor
class HipotecaMixta:
    def __init__(self, 
            capital_prestado, 
            total_meses,
            meses_a_TIN_fijo,
            TIN_fijo_primeros_meses, 
            diferencial_interés_desde_mes_n_más_1, 
            euríbor_desde_mes_n_más_1): # el TIN es el euríbor + diferencial

        self.nombre = "Mixta"
        self.capital_prestado = capital_prestado
        self.total_meses = total_meses
        self.meses_a_TIN_fijo = meses_a_TIN_fijo
        self.TIN_fijo_primeros_meses = TIN_fijo_primeros_meses
        self.diferencial_interés_desde_mes_n_más_1 = diferencial_interés_desde_mes_n_más_1
        self.euríbor_desde_mes_n_más_1 = euríbor_desde_mes_n_más_1

    def hipoteca_primeros_n_meses(self):
        nombre = "Primeros "+str(self.meses_a_TIN_fijo)+" meses"
        return Hipoteca(nombre, self.capital_prestado, self.total_meses, self.TIN_fijo_primeros_meses)

    def hipoteca_desde_mes_n_más_1(self, hipoteca_primeros_n_meses):
        TIN_desde_mes_n_más_1 = self.euríbor_desde_mes_n_más_1 + self.diferencial_interés_desde_mes_n_más_1
        return self.hipoteca_primeros_n_meses().revisa_hipoteca_después_de_n_pagos(self.meses_a_TIN_fijo, TIN_desde_mes_n_más_1)

    def formato_chulo(self):
        hipoteca_primeros_n_meses = self.hipoteca_primeros_n_meses()
        hipoteca_desde_mes_n_más_1 = self.hipoteca_desde_mes_n_más_1(hipoteca_primeros_n_meses)
        return hipoteca_primeros_n_meses.formato_chulo() + "\n" + hipoteca_desde_mes_n_más_1.formato_chulo()
        
