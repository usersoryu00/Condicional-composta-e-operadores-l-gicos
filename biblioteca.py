
anuidade = input("A anuidade está em dia? (sim/não): ").strip().lower()
livros_atrasados = int(input("Quantos livros você tem atrasados?: "))


if anuidade == "sim" and livros_atrasados <= 3:
    print("Parabéns! Você pode pegar livros")
else:
    print("Infelizmente, você precisa regularizar sua situação.")
