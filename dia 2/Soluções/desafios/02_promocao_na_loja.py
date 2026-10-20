precos = [50.0, 120.0, 80.0, 200.0, 100.0]
precos_finais = []
total = 0

for preco in precos:
    if preco >= 100:
        preco_final = preco * 0.9
    else:
        preco_final = preco

    #Cada produto é adicionado à lista, com ou sem desconto.
    precos_finais.append(preco_final)
    total = total + preco_final

print("Preços finais:", precos_finais)
print(f"Valor total da compra: R$ {total:.2f}")
