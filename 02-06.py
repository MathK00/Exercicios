v1 = int(input("Digite o 1° número: "))
v2 = int(input("Digite o 2° número: "))
v3 = int(input("Digite o 3° número: "))
if v1 > v2 and v1 > v3:
    maior=v1
if v2 > v1 and v2 > v3:
    maior=v2
if v3 > v1 and v3 > v2:
    maior=v3
print("O maior número é o: {}". format(maior))
