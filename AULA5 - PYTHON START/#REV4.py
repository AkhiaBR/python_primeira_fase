#REV4

nome = str(input("Nome do funcionário: "))
salario = float(input("Insira o valor de seu salário mensal: "))
print("Siglas de departamento disponíveis: V (VENDAS), C (COMPRAS), P (PRODUÇÃO)")
dep = str(input("Insira a sigla do seu departamento: "))

if (dep == "V"):
    print("O seu salário final é de: ", salario+(salario*(10/100)))
elif (dep == "C"):
    print("O seu slário final é de: ", salario+(salario*(8/100)))
elif (dep == "P"):
    print("O seu salário final é de: ", salario+(salario*(15/100)))
