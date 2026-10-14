def remove_nome(lista: list[str], ind: int) -> None:
    '''
    Remove um cliente na posição 'ind' da lista de nomes
    >>> lista = ["Arthur", "Cintia", "Giovana", "Bernardo", "Claudio"]
    >>> remove_nome(lista, 4) #lista agora é: ["Arthur", "Cintia", "Giovana", "Bernardo"]
    '''
    lista.pop(ind)

def remove_gasto(lista: list[float], ind: int) -> None:
    '''
    Remove os gastos de um cliente no índice 'ind' da lista de gastos
    >>> lista = [400.00, 300.00]
    >>> remove_gasto(lista, 1) #lista agora é: [400.00]
    '''
    lista.pop(ind)

def remove_codigo(lista: list[int], ind: int) -> None:
    '''
    Remove o código de cadastro de um cliente localizado em 'ind'
    na lista de códigos de cadastro de clientes
    >>> lista = [4, 6, 9]
    >>> remove_codigo(lista, 1) #lista agora é: [4, 9]
    '''
    lista.pop(ind)