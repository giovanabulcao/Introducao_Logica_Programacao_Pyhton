def saudacao(nome: str) -> None:
    print("Bom dia {nome}, como está?")

def saudacao_noite(nome: str) -> None:
    print("Boa noite {nome}, como está?")


def determina_sinal(num: int) -> int:
    if num == 0:
        return 0
    elif num > 0:
        return 1
    else:
        return -1