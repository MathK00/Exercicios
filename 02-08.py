v1 = int(input("Digite o 1° valor: "))
v2 = int(input("Digite o 2° valor: "))
v3 = int(input("Digite o 3° valor: "))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print("PODEM formar um triangulo ", end="")
    if v1 == v2 == v3:
        print("EQUILÁTERO!")
    elif v1 != v2  != v3 != v1:
        print("ESCALENO")
    else:
        print("ISÓCELES")       
else:
    print("NÃO PODEM formar um triangulo!")
