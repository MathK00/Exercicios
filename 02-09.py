ca = float(input("Digite o cateto adjacente: "))
co = float(input("Digite o cateto oposto: "))
h = float(input("Digite a hipotenusa: "))
if (ca ** ca) + (co ** co) == (h ** h):
    print("PODEM formar um TRIANGULO RETANGULO")
else: 
    print("NÃO PODEM formar um TRIANGULO RETANGULO")  