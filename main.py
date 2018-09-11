from hipoteca import Hipoteca

def main():

    # préstamo inicial
    C = 200000 
    años = 30
    euríbor = 1.231
    diferencial_interés = 0.39

    meses = años * 12
    TIN = euríbor + diferencial_interés

    hipoteca_inicial = Hipoteca(C, meses, TIN)

    print(hipoteca_inicial.pretty_format())
    
    ## revisión de hipoteca después de n pagos
    n = 12 # un año
    euríbor_1 = 4
    diferencial_interés_1 = 0.39
    nuevo_TIN = euríbor_1 + diferencial_interés_1

    #### hipoteca_revisada = hipoteca_inicial.revisa_hipoteca_después_de_n_pagos(n, nuevo_TIN)


if __name__ == "__main__":
    main()

