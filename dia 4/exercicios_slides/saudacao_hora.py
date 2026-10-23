from funcao1 import saudacao, saudacao_noite

def define_saudacao(nome: str, periodo: str) -> None:
    '''
    Printa a saudação correta para um usuário de nome 'nome' de acordo com o período informado
    a entrada para periodo deve ser 'n' ou 'N' para noite e 'd' ou 'D' para dia
    >>> define_saudacao("Arthur", "d")
    "Bom dia Arthur, como está?"
    >>> define_saudacao("Bernardo", "D")
    "Bom dia Bernardo, como está?"
    >>> define_saudacao("Cintia", "n")
    "Boa noite Cintia, como está?"
    >>> define_saudacao("Giovana", "N")
    "Boa noite Giovana, como está?"
    >>> define_saudacao("Nicolas", "d")
    "Bom dia Nicolas, como está?"
    >>> define_Saudacao("Marcelo", "x")
    "Opção de período inválida!"
    '''
    if periodo == "n" or periodo == "N":
        saudacao_noite(nome)
    elif periodo == "d" or periodo == "D":
        saudacao(nome)
    else:
        print("Opção de período inválida!")