idade = int(input("Digite a idade: "))
estudante = str(input("É estudante? (sim/nao): "))

# A regra da idade tem prioridade sobre a condição de estudante.
if idade <= 12 or idade > 60:
    preco = 15.0
elif estudante == "sim":
    preco = 20.0
else:
    preco = 30.0

print(f"Preço do ingresso: R$ {preco:.2f}") #.2f retorna o numero com apenas duas casas após a virgula
