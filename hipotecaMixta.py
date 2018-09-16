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

        self.nombre = "HIPOTECA MIXTA"
        self.capital_prestado = capital_prestado
        self.total_meses = total_meses
        self.meses_a_TIN_fijo = meses_a_TIN_fijo
        self.TIN_fijo_primeros_meses = TIN_fijo_primeros_meses
        self.diferencial_interés_desde_mes_n_más_1 = diferencial_interés_desde_mes_n_más_1
        self.euríbor_desde_mes_n_más_1 = euríbor_desde_mes_n_más_1
        
        self.hipoteca_primeros_n_meses_a_TIN_fijo = None
        self.hipoteca_desde_mes_n_más_1 = None

        self.total_a_devolver = None
        self.total_porciento_intereses_a_devolver = None

        self.inicializa()

    def inicializa(self):
        # el order de inicialización es importante!
        self.hipoteca_primeros_n_meses_a_TIN_fijo = self.__calcula_hipoteca_primeros_n_meses_a_TIN_fijo()
        self.hipoteca_desde_mes_n_más_1 = self.__calcula_hipoteca_desde_mes_n_más_1(self.hipoteca_primeros_n_meses_a_TIN_fijo)
        self.total_a_devolver = self.__calcula_total_a_devolver()
        self.total_porciento_intereses_a_devolver = self.__calcula_total_intereses_a_devolver()

    def __calcula_hipoteca_primeros_n_meses_a_TIN_fijo(self):
        return Hipoteca(self.nombre, self.capital_prestado, self.total_meses, self.TIN_fijo_primeros_meses)

    def __calcula_hipoteca_desde_mes_n_más_1(self, hipoteca_primeros_n_meses_a_TIN_fijo):
        TIN_desde_mes_n_más_1 = self.euríbor_desde_mes_n_más_1 + self.diferencial_interés_desde_mes_n_más_1
        return hipoteca_primeros_n_meses_a_TIN_fijo.revisa_hipoteca_después_de_n_pagos(self.meses_a_TIN_fijo, TIN_desde_mes_n_más_1)

    def __calcula_total_a_devolver(self):
        total_primeros_n_meses = self.hipoteca_primeros_n_meses_a_TIN_fijo.total_a_devolver()
        total_desde_mes_n_más_1 = self.hipoteca_desde_mes_n_más_1.total_a_devolver()
        return total_primeros_n_meses + total_desde_mes_n_más_1

    def __calcula_total_intereses_a_devolver(self):
        return (self.total_a_devolver - self.capital_prestado)*100/self.capital_prestado

    def formato_chulo(self):
        cabecera_hipoteca_1 = "************ "+self.hipoteca_primeros_n_meses_a_TIN_fijo.nombre+" - Primeros "+str(self.meses_a_TIN_fijo/12)+" años"
        hipoteca_1 = "\n" + self.hipoteca_primeros_n_meses_a_TIN_fijo.formato_chulo()
        cabecera_hipoteca_2 = "\n\n************ "+self.hipoteca_desde_mes_n_más_1.nombre+" - A partir de los "+str(self.meses_a_TIN_fijo/12)+" años"
        hipoteca_2 = "\n" + self.hipoteca_desde_mes_n_más_1.formato_chulo()
        hipoteca_2_euribor = "\nEuríbor: " + str(self.euríbor_desde_mes_n_más_1)
        totales_a_devolver = "\n\nTotal a devolver: " + str(self.total_a_devolver) + " ("+str(self.total_porciento_intereses_a_devolver)+" %)"
        pie = "\n___________________________________________"

        return cabecera_hipoteca_1 + hipoteca_1 + cabecera_hipoteca_2 + hipoteca_2 + hipoteca_2_euribor + totales_a_devolver + pie
