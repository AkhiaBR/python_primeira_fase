nome = []
saldo = []
contador = 0 

while (contador < 2):
    contador += 1
    valor1 = str(input("Digite o nome da pessoa: "))
    valor2 = float(input("Digite o salário dessa pessoa: "))
    nome.append(valor1)
    saldo.append(valor2)



print("Tabela com dados dos funcionários: ")
print("Nome Cliente         Saldo Conta")
print(nome[0], "            ", saldo[0])
print(nome[1], "            ", saldo[1])