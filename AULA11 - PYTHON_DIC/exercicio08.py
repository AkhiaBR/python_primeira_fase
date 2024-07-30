#exercicio09

amigos = {}

for i in range(2):
    nome = str(input("Digite o nome do nome do amigo: "))
    telefone = int(input("Digite o telefone desse amigo: "))
    amigos[nome] = telefone

print(amigos)
print("----------------")

x = str(input("Digite o nome de um novo amigo: "))
y = int(input("Digite o número de teefone desse amigo: "))
amigos.update({x: y})

print(amigos)