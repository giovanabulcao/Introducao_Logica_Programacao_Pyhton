import funcao1


def sinal_lista(lista: list[int]) -> list[int]:
    '''
    Confere o sinal de todos os elementos de uma lista e retorna uma outra lista
    com os sinais dos elementos
    >>> sinal_lista([1, 5, -6, -8, 3])
    [1, 1, -1, -1, 1]
    >>> sinal_lista([0, -3, 1, 0])
    [0, -1, 1, 0]
    '''
    lista_sinal = []
    for i in lista:
        lista_sinal.append(funcao1.determina_sinal(i))