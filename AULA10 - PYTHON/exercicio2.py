frutas = []
estoque = []
preco = []
contador = 0

while contador < 2:
    contador += 1
    valor1 = str(input("Digite o nome da fruta: "))
    valor2 = int(input("Digite o estoque dessa fruta: "))
    valor3 = float(input("Digite o valor da fruta: "))
    frutas.append(valor1)
    estoque.append(valor2)
    preco.append(valor3)
    print("----------------------------------------------------------")

maiorFruta = max(estoque)
menorFruta = min(estoque)

print("Fruta                Quantidade              Preço")
print(frutas[0], "        ", estoque[0], "     ", preco[0])
print(frutas[1], "        ", estoque[1], "     ", preco[1])

print("Fruta com maior quantidade no estoque: ", frutas[estoque.index(maiorFruta)])
print("Fruta com menor quantidade no estoque: ", frutas[estoque.index(menorFruta)])
print("----------------------------------------------------------------------------")
print("Soma dos valores: ", sum(preco))
