
def adiciona_nome(lista_nome_c: list[str], nome_c: str) -> None:
    '''
    Adiciona um nome 'nome_c' à uma lista de nomes de clientes 'lista_nome_c', a adição é feita ao final da lista
    e apenas modifica a lista já existente
    Exemplos:
    >>> lista_nomes = []
    >>> adiciona_nome(lista_nomes, "Marcos") # ["Marcos"]
    >>> adiciona_nome(lista_nomes, "Sandra") # ["Marcos", "Sandra"]
    ''' 
    lista_nome_c.append(nome_c)


def adiciona_cod(lista_cod_c: list[int], cod_c: int) -> None:
    '''
    Adiciona um novo código de cadastro de um cliente 'cod_c' à lista de códigos de cadastro 
    de clientes da loja
    >>> lista_cod = []
    >>> adiciona_cod(lista_cod, 12) # [12]
    >>> adiciona_cod(lista_cod, 90) # [12, 90]
    '''
    lista_cod_c.append(cod_c)


def adiciona_gasto(lista_gasto: list[float], gasto: float) -> None:
    '''
    Adiciona o valor de gasto 'gasto' de um cliente à lista de gastos de clientes da loja 
    >>> lista_g = []
    >>> adiciona_gasto(lista_g, 550.50) # [550.50]
    >>> adiciona_gasto(lista_g, 200.99) # [550.50, 200.99]
    '''
    while gasto < 0:
            gasto = float(input("Valor de gasto negativo!! Insira novamente: "))
    lista_gasto.append(gasto)