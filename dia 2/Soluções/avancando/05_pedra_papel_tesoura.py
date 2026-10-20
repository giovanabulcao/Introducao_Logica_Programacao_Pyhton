jogada1 = input("Jogador 1 (pedra/papel/tesoura): ")
jogada2 = input("Jogador 2 (pedra/papel/tesoura): ")

# Verifica as entradas antes de determinar o vencedor.
if jogada1 != "pedra" and jogada1 != "papel" and jogada1 != "tesoura":
    print("Entrada inválida do Jogador 1.")
elif jogada2 != "pedra" and jogada2 != "papel" and jogada2 != "tesoura":
    print("Entrada inválida do Jogador 2.")
elif jogada1 == jogada2:
    print("Empate")
elif jogada1 == "pedra" and jogada2 == "tesoura":
    print("Jogador 1 venceu")
elif jogada1 == "tesoura" and jogada2 == "papel":
    print("Jogador 1 venceu")
elif jogada1 == "papel" and jogada2 == "pedra":
    print("Jogador 1 venceu")
else:
    print("Jogador 2 venceu")
