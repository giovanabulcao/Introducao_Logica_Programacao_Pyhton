def calcula_media(notas: list[float]) -> float:
    total = 0
    for i in notas:
        total += i
    
    media = total / len(notas)

    return media

def situacao(media: float) -> None:
    if media < 5.0:
        print("Aluno Reprovado")
    elif media < 6.0:
        print("Aluno de Recuperação")
    else:
        print("Aluno Aprovado")
