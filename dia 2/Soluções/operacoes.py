a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

print()
print('Escolha um simbolo para fazer uma operação matemática: ')
print('+ Soma')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')

op = str(input())

if op == '+':
    print('Soma: ', a+b)
elif op == '-':
    print('Subtração: ', a-b)
elif op == '*':
    print('Multiplicação: ', a*b)
elif op == '/':
    if b == 0:
        print('Erro. Não é possível realizar uma divisão por 0.')
    else:
        print('Divisão: ', a/b)
else:
    print('Operação Inválida. Tente novamente.')


