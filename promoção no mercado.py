
total_compra = float(input("Digite o valor total da compra (R$): "))

itens_hortifruti = int(input("Digite a quantidade de itens de hortifruti comprados: "))



if total_compra >= 100 and itens_hortifruti >= 3:
    print("Cliente recebe o desconto!")
else:
    print("Cliente NÃO recebe o desconto.")
