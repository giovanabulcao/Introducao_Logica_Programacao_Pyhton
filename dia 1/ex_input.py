''' 1) Faça um programa que pergunta qual é a data.'''

data = input("Qual a data de hoje? dd/mm/aaaa ")
# OPCIONAL
print(data)
print(f"A data de hoje é: {data}")
print("A data de hoje é: ", data)
print("A data de hoje é: " + data)

#=========================================================================

'''2) Faça um programa que pergunte o nome do usuário,
sua idade e sua comida favorita.'''

nome = input("Qual seu nome? R:")
# Observe que a idade deve ser um número inteiro!
idade = int(input("Quantos anos você tem? R:")) 
comida_favorita = input("Qual sua comida favorita? R:")

# OPCIONAL
print(f'\nNome: {nome} \nIdade: {idade} \nComida Favorita:{comida_favorita}') 
print("\nNome: ", nome, "\nIdade: ", idade, "\nComida Favorita: ", comida_favorita)

#==========================================================================

'''3)Faça um programa que printa 3x o que o usuário inserir no terminal'''

alguma_coisa = input("Digite o que desejar ;)")

print(alguma_coisa)
print(alguma_coisa)
print(alguma_coisa)

# Ou também

print(alguma_coisa, alguma_coisa, alguma_coisa)