lista = []
tamanho = int(input("Qual o tamanho da sua lista? "))

for _ in range(tamanho):
    elemento = int(input("Qual o valor a ser inserido na lista? "))
    lista.append(elemento)

print(lista)