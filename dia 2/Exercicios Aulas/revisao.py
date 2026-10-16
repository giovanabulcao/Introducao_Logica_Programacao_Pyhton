nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))

print()

media = (nota1 + nota2)/ 2.0

aprovado = (media>=6.0) and (faltas <= 5)

print("-------BOLETIM--------")
print("Aluno: ", nome)
print("Média Final: ", media)
print("Quantidade de Faltas: ", faltas)
print("Aprovado: ", aprovado)

