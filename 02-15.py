opção = 0
while opção != 5:
    print('''    [1] Triângulo
    [2] Quadrado
    [3] Retângulo
    [4] Círculo
    [5] Fim do processo''') 
    opção = int(input(">>>>> Qual a sua opção?: "))
    if opção == 1:
        b = int(input("Insira o valor da base: "))
        h = int(input("Insira o valor da hipotenusa: "))
        t = b * h / 2
        print("A área do triângulo é: ", t)
    elif opção == 2:
        l = int(input("Insira o valor do lado: "))
        q = l ** 2
        print("A área do quadrado é de: ", q)
    elif opção == 3:
        b = int(input("Insira o valor da base: "))
        a = int(input("Insira o valor da altura: "))
        a = b * a
        print("A área do retângulo é de: ", a)
    elif opção == 4:
        r = int(input("Insira o valor do raio: "))
        import math
        a = math.pi*r ** 2
        print("A área do círculo é de: ", a)
    elif opção ==5:
        print("Finalizando...")
    else:
        print("Opção Invalida. Tente novamente")
    print("=-=" * 10)
print("Fim do programa!")        
