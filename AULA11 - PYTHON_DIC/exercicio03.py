#exercicio 03

produtos = {}

for i in range(5):
    nome = str(input("Digite o nome do produto: "))
    preco = int(input("Digite o preço referente ao produto: "))
    produtos[nome] = preco

print(produtos)