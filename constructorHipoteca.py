from hipotecaMixta import HipotecaMixta

class ConstructorHipoteca:
    def __init__(self):
        return

    @staticmethod
    def crea_hipoteca_mixta():

        # préstamo inicial
        C = 220000 
        total_años = 38
        total_meses = total_años * 12
        
        ## Condiciones primeros diez años
        meses_10_años = 10 * 12
        TIN_fijo_10_años = 1.69

        ## Condiciones a partir de año 11
        euríbor_desde_año_11 = 2
        diferencial_interés_desde_año_11 = 0.99

        hipoteca_mixta = HipotecaMixta(C, total_meses, meses_10_años, TIN_fijo_10_años, diferencial_interés_desde_año_11, euríbor_desde_año_11)
    
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
        euríbor_desde_año_2 = 2
        diferencial_interés_desde_año_2 = 0.89

        hipoteca_variable = HipotecaMixta(C, total_meses, meses_1_año, TIN_fijo_1_año, diferencial_interés_desde_año_2, euríbor_desde_año_2)

        return hipoteca_variable
