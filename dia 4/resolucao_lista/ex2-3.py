import datetime as dt

def define_idade(ano: int) -> int:
    return dt.date.today().year - ano

def confere_maioridade(idade: int) -> None:
    if idade < 18:
        print("Menor de Idade")
    else:
        print("Maior de Idade")

