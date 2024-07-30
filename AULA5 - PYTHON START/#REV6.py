#REV6

nome = str(input("Insira seu nome: "))
salariofix = float(input("Insira o valor do salário fixo mensal: "))
vendas = int(input("Insira o número de vendas realizadas no mês: "))
comissao = salariofix+((vendas/100)*15)

print(nome, "o valor final do salário será de: ", comissao)