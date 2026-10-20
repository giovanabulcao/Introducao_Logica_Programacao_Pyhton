numeros:list[int] = [4, 8, 15, 16, 23, 42]
total = 0

for numero in numeros:
    total = total + numero

# Fora do laço: imprime o total somente depois de somar todos os números.
print("Total:", total)
