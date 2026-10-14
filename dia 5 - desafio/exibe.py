def exibe_formatado(cod: list[int], nomes: list[str], gasto: list[float]) -> None:
    '''
    exibe todos os clientes cadastrados e seus dados de maneira formatada para
    melhor visualização
    '''

    qtde_clientes = len(cod)

    for i in range(qtde_clientes):
        print("-----------------------")
        print("Número de Cadastro: ", cod[i])
        print("Nome: ", nomes[i])
        print("Total Gasto: ", gasto[i])
        print("-----------------------")