sexo = str(input("Qual é o seu gênero [M/F]: "))
peso = float(input("Qual o seu peso?"))
altura = float(input("Digite a sua altura"))
meso = peso / (altura * altura)
if "M":
    print("Sua relação peso/altura", massa)
    if massa < 20:
        print("Abaixo do peso.")
    elif 20 <= massa < 28:
        print("Peso ideal.")  
    else:
        print("Acima do peso.")
else:
    print("Sua relação peso/altura", massa)
    if massa < 19:
        print("Abaixo do peso.") 
    elif 19 <= massa < 24:
        print("Peso ideal.")
    else:
        print("Acima do peso.") 
print("Aperte qualquer tecla para sair.")               
