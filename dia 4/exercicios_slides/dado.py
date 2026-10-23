import random as rd

def dado() -> None:
    valor = rd.randint(1, 20)
    if 1 <= valor <= 5:
        print("Muito Fraco")
    elif 5 < valor <= 10:
        print("Fraco")
    elif 10 < valor <= 15:
        print("Médio")
    elif 15 < valor <= 19:
        print("Forte")
    else:
        print("Crítico")


for i in range(30):
    dado()