#exercicio06

mercado = {}

for i in range(5):
    nome = str(input("Digite o nome do produto: "))
    preco = int(input("Digite o preço desse produto: "))
    mercado[nome] = preco
    
print(mercado)