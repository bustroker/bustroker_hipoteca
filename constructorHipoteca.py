from hipotecaMixta import HipotecaMixta

class ConstructorHipoteca:
    def __init__(self):
        return

    @staticmethod
    def crea_hipoteca_mixta(estimación_euríbor_desde_año_11 = 2):

        # préstamo inicial
        C = 220000 
        total_años = 38
        total_meses = total_años * 12
        
        ## Condiciones primeros diez años
        meses_10_años = 10 * 12
        TIN_fijo_10_años = 1.79

        ## Condiciones a partir de año 11
        estimación_euríbor_desde_año_11 = 0.8
        diferencial_interés_desde_año_11 = 0.99

        hipoteca_mixta = HipotecaMixta(C, total_meses, meses_10_años, TIN_fijo_10_años, diferencial_interés_desde_año_11, estimación_euríbor_desde_año_11)
    
        return hipoteca_mixta

    @staticmethod
    def crea_hipoteca_variable():## funciona como una mixta con TIN fijo el primer año
        
        # préstamo inicial
        C = 220000 
        total_años = 38
        total_meses = total_años * 12
        
        ## Condiciones primer año
        meses_1_año = 12
        TIN_fijo_1_año = 1.99

        ## Condiciones desde segundo año
        estimación_euríbor_desde_año_2 = 1
        diferencial_interés_desde_año_2 = 0.89

        hipoteca_variable = HipotecaMixta(C, total_meses, meses_1_año, TIN_fijo_1_año, diferencial_interés_desde_año_2, estimación_euríbor_desde_año_2)

        return hipoteca_variable
