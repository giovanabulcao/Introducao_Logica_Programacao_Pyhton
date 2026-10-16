#Projete um programa que recebe dois números e retorna o menor deles.

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

if a < b:
    print(f'O menor número entre {a} e {b} é: {a}')
else: 
    print(f'O menor número entre {a} e {b} é: {b}')