notas = [8.0, 4.5, 6.0, 9.0, 3.0, 5.5, 7.0]
aprovados = 0
recuperacao = 0
reprovados = 0

for nota in notas:
    if nota >= 6:
        print(nota, "- Aprovado")
        aprovados = aprovados + 1
    elif nota >= 4:
        # Só chegamos aqui se a nota for menor que 6.
        print(nota, "- Recuperação")
        recuperacao = recuperacao + 1
    else:
        print(nota, "- Reprovado")
        reprovados = reprovados + 1

print("Aprovados:", aprovados)
print("Em recuperação:", recuperacao)
print("Reprovados:", reprovados)
