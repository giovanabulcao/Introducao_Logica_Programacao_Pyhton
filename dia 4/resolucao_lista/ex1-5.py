saldo = 550.00
print(saldo)
def desconta10(valor: float) -> float:
    return valor - (valor/10)

desconta10(saldo)
print(saldo)

'''
Não acontece nada, pois dentro da função é criada uma nova variável com o mesmo valor
da variável saldo, logo, a variável saldo em si não muda
'''