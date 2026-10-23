from math import sqrt

def pitagoras(a: int, b: int) -> float:
    '''
    Acha o valor da hipotenusa através do teorema de pitágoras,
    temos como entrada dois valores inteiros, e o retorno é um valor de ponto flutuante
    >>> pitagoras(2, 3)
    3.6055
    >>> pitagoras(3, 4)
    5.0
    >>> pitagoras(0, 3)
    3.0
    '''
    c = sqrt((a**2) + (b**2))
    return c

print(pitagoras(2, 3))
print(pitagoras(3, 4))
print(pitagoras(0, 3))