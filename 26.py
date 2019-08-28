n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opção = 0
while opção != 5:
    print('''    [1] Multiplicação
    [2] Adição
    [3] Divisão
    [4] Subtração
    [5] Fim do processo''')
    opção = int(input(">>>>> Qual a sua opção?: "))
    if opção == 1:
        multiplicar = n1 * n2
        print("A multiplicação entre {} e {} é de: {}".format(n1, n2, multiplicar))
    elif opção == 2:
        soma = n1 + n2
        print("A soma entre {} e {} é de: {}".format(n1, n2, soma))
    elif opção == 3:
        if n2== 0:
            print("Erro")
        dividir = n1 / n2
        print("A divisão entre {} e {} é de {}".format(n1, n2, dividir))
    elif opção == 4:
        subtrair = n1 - n2
        print("A subtração entre {} e {} é de".format(n1, n2, subtrair))
    elif opção ==5:
        print("Finalizando...")
    else:
        print("Opção Invalida. Tente novamente")
    print("=-=" * 10)
print("Fim do programa!")                       