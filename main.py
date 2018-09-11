from calculadora import Calculadora

def main():
    c_0 = 200000 # préstamo
    años = 30

    euríbor = 1.231 # euribor
    diferencial_interés = 0.39

    TIN = euríbor + diferencial_interés

    # interés efectivo mensual (divido tb por 100 para tener el por-uno)
    i = TIN / 1200 

    # total de cuotas
    N = años * 12 # meses

    calculadora = Calculadora

    # cuota
    c_1 = calculadora.cuota(c_0, i, N)

    # capital pendiente de amortización después de 12 cuotas pagadas
    C_12 = calculadora.deuda_despues_de_n_pagos(c_1, i, N, 12)

    # nueva cuota de hipoteca a N-12 por el importe C_12

    print(C_12)


if __name__ == "__main__":
    main()

