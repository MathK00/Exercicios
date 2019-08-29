p = float(input("Valor da bolsa: "))
a = p * 0.9
b = p / 3
c1 = p + (p*5/100)
c2 = c1 / 10
print ("A vista com 10% de desconto = R$:{}" .format (a))
print ("Parcelado em 1 + 2 vezes sem desconto = R$:{} " .format (b))
print ("Dividido em 10 vezes com juros de 5% sobre o valor da parcela R$:{} valor total é de R$:{}" .format (c2, c1))
