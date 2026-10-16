#Projete um programa que determine o sinal de um número, produzindo -1 para valores negativos, 1 para valores positivos e 0 para o 0.

num = int(input('Digite um número: '))

if num < 0: #Se *num* for menor que 0, ele é negativo
    print(-1)
elif num > 0:
    print(1)
else:
    print(0)
    