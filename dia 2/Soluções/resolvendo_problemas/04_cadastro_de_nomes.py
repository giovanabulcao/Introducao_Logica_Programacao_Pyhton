#Recebe uma lista vazia e retorna uma lista de nomes 'cadastrados' e a quantidade de nomes cadastrados

nomes:list[str] = []

nome = str(input("Digite o primeiro nome: "))
nomes.append(nome)

nome = str(input("Digite o segundo nome: "))
nomes.append(nome)

nome = str(input("Digite o terceiro nome: "))
nomes.append(nome)

nome = str(input("Digite o quarto nome: "))
nomes.append(nome)

print("Nomes cadastrados:", nomes)
print("Quantidade de nomes:", len(nomes)) 
