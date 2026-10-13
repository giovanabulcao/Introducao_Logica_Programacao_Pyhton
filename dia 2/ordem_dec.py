n1 = int(input())
n2 = int(input())
n3 = int(input())

print("Números em ordem decrescente:")
if (n1 != n2) and (n1 != n3) and (n2!=n3): #verifica se todos são diferentes
    if n1 > n2 and n1 > n3:
        if n2 > n3:
            print(n1, n2, n3)
        else:
            print(n1, n3, n2)
    elif n2 > n1 and n2 > n3:
        if n1 > n3:
            print(n2, n1, n3)
        else:
            print(n2, n3, n1)
    else:
        if n1 > n2:
            print(n3, n1, n2)
        else:
            print(n3, n2, n1)
        
else:
    print("Os números precisam ser todos diferentes!")


# 1 2 3 -> 3 2 1
# 4 6 1 -> 6 4 1
# 7 5 6 -> 7 6 5