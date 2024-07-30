#exercicio6

contador = 0
aprovados = 0
reprovados = 0

while contador < 50:
    contador += 1
    media = float(input("Digite a média do aluno: "))

    if media < 7:
        reprovados += 1
    elif media >= 7 and media <= 10:
        aprovados += 1

print("Número de alunos aprovados: ", aprovados, ",", "número de alunos reprovados: ", reprovados)