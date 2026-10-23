import operacoes # chamada do arquivo 'operacoes.py' 


def menor_que_vinte(num: int) -> bool:
    '''
    Confere se um número 'num' é maior que 20
    '''
    menor = False
    if num < 20:
        menor = True
    return menor

def main():
    print("Soma 2 + 10 =", operacoes.somanum(2, 10)) # chamada das funções contida no arquivo importado
    print("Subtração 5 - 2 =", operacoes.sub(5, 2))
    variavel_z = operacoes.variavel_x + operacoes.variavel_y
    print("\nVariavel x é menor que 20?\n", menor_que_vinte(operacoes.variavel_x))
    variavel_x = variavel_z
    print("\nVariavel x é menor que 20?\n", menor_que_vinte(operacoes.variavel_x))

if __name__ == "__main__":
    main()