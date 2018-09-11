from hipotecaVariable import HipotecaVariable

def main():

    # préstamo inicial
    C = 200000 
    años = 30
    
    ## Condiciones primer año
    euríbor = 1.231
    diferencial_interés = 0.39
    TIN_año_1 = euríbor + diferencial_interés

    ## Condiciones segundo año
    euríbor_desde_año_2 = 4
    diferencial_interés_desde_año_2 = 0.39

    meses = años * 12

    hipoteca_variable = HipotecaVariable(C, meses, TIN_año_1, diferencial_interés_desde_año_2, euríbor_desde_año_2)

    print(hipoteca_variable.formato_chulo())

if __name__ == "__main__":
    main()

