sexo = str(input("Qual é o seu gênero [M/F]: "))
peso = float(input("Qual o seu peso?"))
altura = float(input("Digite a sua altura"))
massa = peso / (altura * altura)
if (altura => 2.50):
    print("AVATAR!!!")
if "M":
    print("Sua relação peso/altura", massa)
    if massa < 20:
        print("Abaixo do peso.")
    elif 20 <= massa < 25:
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
