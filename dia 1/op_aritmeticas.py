''' 1) Calcule o resto da divisão de 14 por 3 e imprima o resultado na tela.'''

divisao: float = 14 / 3
print("Resultado da divisão: ", divisao)

#================================================================

''' 2) Faça um programa que o usuário insere um valor em reais e o programa mostra na tela em dólares.
Considere 5 reais = 1 dólar. '''

reais = float(input("Digite um valor em reais: "))
dolar = reais * 5

print(reais, "reais equivale a", dolar, "dolares.")

#==================================================================

''' 3) Faça um programa que calcula a fórmula de bhaskara,
o usuário insere os valores de a, b e c e o programa
retorna o valor de x’ e x’’  '''

a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))
c = float(input("Digite mais um valor kk: "))

delta = b*b - (4 * a * c) # delta = b² - 4.a.c

x1 = -b + (delta ** 1/2)  # -b + (delta¹/²)
x2 = -b - (delta ** 1/2)    

print("X’ = ", x1)
print("X’’ = ", x2)
