#exercicio01

d = {}
x = int(input("Digite quantas pessoas deseja cadastrar: "))

for i in range(x):
    nome = str(input("Digite um nome: "))
    idade = int(input("Digite a idade referente: "))

    d[nome] = idade

print(d)