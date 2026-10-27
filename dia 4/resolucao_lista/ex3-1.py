import random as rd

def rola_dado() -> int:
    return rd.randint(1, 20)

def vencedor() -> None:
    vitorias_p1 = 0
    vitorias_p2 = 0
    
    while vitorias_p1 < 3 and vitorias_p2 < 3:
        pontos_p1 = rola_dado()
        print("Rolagem Player 1:", pontos_p1)
        pontos_p2 = rola_dado()
        print("Rolagem Player 2:", pontos_p2)

        if pontos_p1 > pontos_p2:
            vitorias_p1 += 1
            print("-- Rodada do player 1 --\n")
        elif pontos_p1 < pontos_p2:
            vitorias_p2 += 1
            print("-- Rodada do player 2 --\n")
        else:
            print("Rodada empatada\n")
    
    if vitorias_p1 >= 3:
        print("----Vitória Player 1----")
    else:
        print("----Vitória Player 2----")

vencedor()