from constructorHipoteca import ConstructorHipoteca

def main():
    
    # hipoteca_mixta = ConstructorHipoteca.crea_hipoteca_mixta()
    #print(hipoteca_mixta.formato_chulo())

    # hipoteca_variable = ConstructorHipoteca.crea_hipoteca_variable()
    # print(hipoteca_variable.formato_chulo())

    hipoteca = ConstructorHipoteca.crea_hipoteca()
    print(hipoteca.formato_chulo())

if __name__ == "__main__":
    main()

