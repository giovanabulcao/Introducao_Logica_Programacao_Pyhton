# Resultados esperados dos casos do enunciado:
# a = 10, b = 3: A, pois 10 > 3 e 10 > 6.
# a = 5, b = 5: C, pois os números são iguais.
# a = 3, b = 10: D, pois a < b e 10 > 6.
# a = 7, b = 5: B, pois 7 > 5, mas 7 não é maior que 10.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    if a > 2 * b:
        r = "A"
    else:
        r = "B"
elif a == b:
    r = "C"
else:
    if b > 2 * a:
        r = "D"
    else:
        r = "E"

print(r)
