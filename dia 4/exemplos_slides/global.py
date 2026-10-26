x = 15
print(x)

def soma_a(a: int) -> None:
    global x
    x = x + a

    
soma_a(5)
print(x)