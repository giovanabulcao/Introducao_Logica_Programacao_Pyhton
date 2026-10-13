n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite sua nota 2: "))
n3 = float(input("Digite sua nota 3: "))
n4 = float(input("Digite sua nota 4: "))

media_anual = (n1 + n2 + n3 + n4)/ 4.0

if media_anual >= 6.0:
    print("Aluno Aprovado!!")
    print("Média anual = ", media_anual)

