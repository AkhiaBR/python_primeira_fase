#exercicio5

contador = 0
contador1 = 0
contador2 = 0
contador3 = 0

while contador < 100:
    contador += 1
    nome = str(input("Digite seu nome: "))
    salario = float(input("Digite o valor de seu salário mensal: "))

    if salario < 1500:
        contador1 += 1
    elif salario >= 1500 and salario < 3000:
        contador2 += 1
    elif salario >= 3000:
        contador3 += 1

print("O número de pessoas com salário menor que R$ 1.500 é: ", contador1, ", já a de pessoas com salário maior que R$ 1.500 e menor que R$ 3.000: ", contador2, ", já a de pessoas com salário maior que R$ 3.000 é: ", contador3)
