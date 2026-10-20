a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    print("Resultado:", a + b)
elif operacao == "-":
    print("Resultado:", a - b)
elif operacao == "*":
    print("Resultado:", a * b)
elif operacao == "/":
    if b == 0:
        print("Erro: não é possível dividir por zero.")
    else:
        print("Resultado:", a / b)
else:
    print("Operação inválida.")
