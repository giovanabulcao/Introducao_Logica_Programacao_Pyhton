def busca_cliente(lista: list[int], cod: int) -> int:
    '''
    Busca um cliente na lista de clientes e retorna o índice em que ele está posicionado na lista
    >>> lista = [1, 2, 4, 5]
    >>> busca_cliente(lista, 5)
    3
    '''
    for i in range(len(lista)):
        if lista[i] == cod:
            return i

    return -1

def achou(i: int) -> bool:
    '''
    Confere se um elemento foi encontrado na 'busca_cliente'
    '''
    return i != -1

def vazia(lista: list) -> bool:
    '''
    Retorna se uma lista está vazia 
    '''
    return len(lista) == 0

def id_repetido(lista: list[int], cod: int) -> bool:
    '''
    Confere se um código já está presente na lista de códigos de clientes,
    será utilizada para impedir que usuários sejam cadastrados com id's duplicados
    '''
    for i in lista:
        if cod == i:
            return True
    return False