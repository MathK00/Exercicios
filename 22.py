peso_h = 0
altura_h = 0
peso_m = 0
altura_m = 0
peso = float(input("Coloque o peso em (KG): "))
altura = float(input("Coloque a altura em (CM): "))
genero = str(input("Coloque o sexo da pessoa (M) ou (F): "))
if genero.upper() == "M": 
    peso_h += peso
    altura_h += altura
elif genero.upper() =="F":
    peso_m += peso
    altura_m += altura
else:
    print("O sexo selecionado não é o correto. Tente novamente")
     
       