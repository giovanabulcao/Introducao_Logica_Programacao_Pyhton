
# Seleção simples: executa um bloco apenas quando a condição é verdadeira.
# Seleção composta: escolhe entre dois caminhos, usando if e else.
# Seleção encadeada: verifica condições em sequência, usando if, elif e else.
# A diferença está na quantidade de caminhos e condições considerados.

idade = int(input("Digite sua idade: "))

# Exemplo de seleção simples.
if idade >= 18:
    print("Você é maior de idade.")

# Exemplo de seleção composta.
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exemplo de seleção encadeada.
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")
