from hipoteca import Hipoteca

def main():

    # préstamo inicial
    C = 200000 
    años = 30
    euríbor = 1.231
    diferencial_interés = 0.39

    meses = años * 12
    TIN = euríbor + diferencial_interés

    hipoteca_inicial = Hipoteca("Inicial", C, meses, TIN)

    print(hipoteca_inicial.formato_chulo())
    
    ## revisión de hipoteca después de n pagos
    n = 12 # un año
    nuevo_euríbor = 4
    nuevo_diferencial_interés = 0.39
    nuevo_TIN = nuevo_euríbor + nuevo_diferencial_interés

    hipoteca_revisada = hipoteca_inicial.revisa_hipoteca_después_de_n_pagos(n, nuevo_TIN)
    print(hipoteca_revisada.formato_chulo())

if __name__ == "__main__":
    main()

