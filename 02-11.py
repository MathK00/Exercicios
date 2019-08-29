v0 = float(input("Insira a velocidade inicial: "))
a = float(input("Insira a velocidade do automóvel: "))
t = float(input("Insira o tempo: "))
v = vo + a * t
if v <= 40:
    print("Veículo muito lento")
elif 40 < V <= 60:
    print("Velocidade permitida")
elif 60 < V <= 80
    print("Velocidade de cruzeiro")
elif: 80 < V <= 120:
    print("Veículo rápido")
else:
    print("Veículo muito rápido")