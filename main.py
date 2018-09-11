from constructorHipoteca import ConstructorHipoteca

def main():
    
    hipoteca_mixta = ConstructorHipoteca.crea_hipoteca_mixta()
    print(hipoteca_mixta.formato_chulo())

    estimación_euríbor_desde_año_2 = 3
    hipoteca_variable = ConstructorHipoteca.crea_hipoteca_variable(estimación_euríbor_desde_año_2)
    #print(hipoteca_variable.formato_chulo())

if __name__ == "__main__":
    main()

