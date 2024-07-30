#exercicio 02

funcionarios = {}
x = int(input("Digite a quantidade de funcionários a serem cadastrados: "))

for i in range(x):
    codigo = int(input("Qual é o código do funcionário?: "))
    nome = str(input("Digite seu respectível nome: "))
    funcionarios[codigo] = nome

print(funcionarios)
print("-----------------")
respostas = str(input("Caso deseje demitir um funcionário, digite sim(S), se não, digite não(N): ")).upper()

if(respostas == "S"):
    demissao = int(input("Digite o código do funcionário que deseja demitir: "))
    funcionarios.pop(demissao)
    print(funcionarios)
