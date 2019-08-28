peso = float(input("Qual é o peso? (KG): "))
altura = float(input("Qual é a sua altura? (M): "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de: {:.1f}".format(imc))
if imc < 20: 
    print("Você está ABAIXO DO PESO")
elif 20 <= imc < 25:
    print("Você está NO PESO IDEAL")
elif imc >= 25: 
    print("Você está ACIMA DO PESO")   
