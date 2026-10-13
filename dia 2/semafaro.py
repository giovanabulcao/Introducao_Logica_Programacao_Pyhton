print("VERMELHO\nAMARELO\nVERDE")
cor = str(input("Digite a cor atual do semáfaro: "))

if cor == "VERMELHO":
    print("parar")
elif cor == "AMARELO":
    print("atenção")
else:
    print("seguir")

