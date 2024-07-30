#exercicio1

contador = 0
contadorm = 0
contadorf = 0

while contador < 3:
    contador += 1
    nome = str(input("Digite seu nome: "))
    sexo = str(input("Qual seu sexo? (M ou F): ")).upper()

    if sexo == "M":
        contadorm += 1
    elif sexo == "F":
        contadorf += 1

print("A quantidade de pessoas do sexo masculino é: ", contadorm, ", já a de pessoas do sexo feminino é: ", contadorf)
