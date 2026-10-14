
def altera_nome(lista_nome: list[str], ind: int, novo_nome: str) -> None:
    '''
    altera o nome do cliente que está no índice 'ind' da lista 
    >>> lista = ["Marcelo"]
    >>> altera_nome(lista, 0, "Pedro") #lista agora é ["Pedro"]
    '''

    lista_nome[ind] = novo_nome



def altera_gasto(lista_gasto: list[float], ind: int, novo_gasto: float) -> None:
    '''
    altera o gasto do cliente que está no índice 'ind' da lista 
    >>> lista = [500.00]
    >>> altera_nome(lista, 0, 565.99) #lista agora é [565.99]
    '''
    
    lista_gasto[ind] = novo_gasto