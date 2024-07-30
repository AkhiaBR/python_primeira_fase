#exercicio05

amigos = {}

for i in range(10):
    nome = str(input("Digite o nome do amigo: "))
    telefone = int(input("Digite o número de telefone desse amigo: "))
    amigos[nome] = telefone

print(amigos)