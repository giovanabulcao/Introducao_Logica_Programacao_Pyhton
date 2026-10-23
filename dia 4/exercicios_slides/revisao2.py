repete = 's'
lista = []
while repete == 's':
    elemento = int(input("Digite um valor a ser inserido na lista: "))
    lista.append(elemento)
    repete = input("Deseja adicionar mais algum elemento à lista?\nSim - s\nNão - n\n>>> ")
print(lista)