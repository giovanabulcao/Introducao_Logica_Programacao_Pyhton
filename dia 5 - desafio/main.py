from adiciona import *
from altera import *
from remove import *
from exibe import *

def busca_cliente(lista: list[int], cod: int) -> int:
    '''
    Busca um cliente na lista de clientes e retorna o índice em que ele está posicionado na lista
    >>> lista = [1, 2, 4, 5]
    >>> busca_cliente(lista, 5)
    4
    '''

    i = 0
    achou = False

    while lista[i] < len(lista) and lista[i] != cod:
        if lista[i] == cod:
            achou = True
        i += 1

    if not achou:
        i = -1

    return i

def vazia(lista: list) -> bool:
    '''
    Retorna se uma lista está vazia 
    '''
    return len(lista) == 0


def menu():
    print("=======================================")
    print("1 - Adicionar Cliente")
    print("2 - Excluir Cliente")
    print("3 - Alterar Cliente")
    print("4 - Exibir Todos Clientes")
    print("5 - Sair")
    print("=======================================")



def main():
    id_clientes = []
    nome_clientes = []
    gasto_clientes = []
    menu()
    opcao = int(input("Bem vindo ao Sistema de Gerenciamento de Clientes!!\nQual operação você quer realizar??\n"))
    continuar = True
    while continuar:
        menu()
        if opcao == 1:
            cod = int(input("Insira o código de cadastro do cliente: "))
            nome = input("Insira o nome do cliente: ")
            gasto = float(input("Insira o gasto do cliente: "))
            adiciona_cod(id_clientes, cod)
            adiciona_nome(nome_clientes, nome)
            adiciona_gasto(gasto_clientes, gasto)
            print("Cliente cadastrado com sucesso!!")
            opcao = int(input("Qual operação você quer realizar??\n"))

        elif opcao == 2:
            if vazia(id_clientes):
                print("Não há clientes cadastrados!!")
            else:
                remove = int(input("Insira o código de cadastro do cliente a ser removido: "))
                cliente = busca_cliente(id_clientes, remove)
                remove_codigo(id_clientes, cliente)
                remove_gasto(gasto_clientes, cliente)
                remove_nome(nome_clientes, cliente)
                print("Cliente removido com sucesso!!")
            opcao = int(input("Qual operação você quer realizar??\n"))
        elif opcao == 3:
            if vazia(id_clientes):
                print("Não há cliente cadastrados!!")
            else:
                altera = int(input("Insira o código de cadastro do cliente a ser alterado: "))
                cliente = busca_cliente(id_clientes, altera)
                alt = int(input("O que você deseja alterar?\n1 - Nome\n2 - Gasto\n>>> "))
                if alt == 1:
                    novo_nome = input("Insira o nome novo a ser cadastrado: ")
                    altera_nome(nome_clientes, cliente, novo_nome)
                elif alt == 2:
                    novo_gasto = float(input("Digite o novo gasto: "))
                    altera_gasto(gasto_clientes, cliente, novo_gasto)
            opcao = int(input("Qual operação você quer realizar??\n"))

        elif opcao == 4:
            if vazia(id_clientes):
                print("Não há clientes cadastrados!!")
            else:
                exibe_formatado(id_clientes, nome_clientes, gasto_clientes)

            opcao = int(input("Qual operação você quer realizar??\n"))
        
        elif opcao == 5:
            continuar = False
            print("Obrigado por utilizar nosso sistema!!")

        


if __name__ == "__main__":
    main()