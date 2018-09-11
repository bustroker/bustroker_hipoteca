class Calculadora:
    def __init__(self):
        return
    
    def interés_efectivo_mensual(self,
            euríbor,
            diferencial_interés):
            
        # (divido tb por 100 para tener el por-uno)
        return (euríbor + diferencial_interés) / 1200

    def cuota(self,
            monto_préstamo, 
            interés_efectivo_mensual, 
            total_de_meses):
        c_0 = monto_préstamo
        i = interés_efectivo_mensual
        N = total_de_meses
        
        return (c_0 * i) / (1-(1 + i)**(-N))

    def deuda_después_de_n_pagos(self,
            monto_cuota, 
            interés_efectivo_mensual, 
            total_de_meses, 
            n):
        c = monto_cuota
        i = interés_efectivo_mensual
        N = total_de_meses

        return c/i * (1 - (1+i)**(n-N))