n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))
n3 = float(input("Digite a 3° nota: "))
print("=-=" * 10) 
me = n1 + n2 + n3
mp = ((n1 * 4) + (n2 * 5) + (n3 * 6 )) / 15
if mp >= 6: 
    print("APROVADO")
elif mp <= 3:
    print("REPROVADO")
elif mp >= 3 <= 5:
    print("EXAME")
print("=-=" * 10)    
exame = float(input("Digite a nota da prova final: "))
print("=-=" * 10)
nf = (mp + exame) / 2
if nf >= 6: 
    print("APROVADO")
else:
    print("REPROVADO")