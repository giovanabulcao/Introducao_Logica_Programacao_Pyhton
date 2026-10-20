notas = [5.5, 7.0, 8.5, 4.0, 6.0]
aprovacoes = 0

for nota in notas:
    if nota >= 6:
        aprovacoes = aprovacoes + 1 #soma 1 toda vez q encontrar uma nota >=6

print("Quantidade de aprovações:", aprovacoes)
