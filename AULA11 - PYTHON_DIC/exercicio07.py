#exercicio07

alunos = {}

x = int(input("Digite a quantidade de alunos a serem cadastradas: "))

for i in range(x):
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite sua primmeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    nota3 = float(input("Digite sua terceira nota: "))
    media = nota1+nota2+nota3/3
    if media < 5:
        print("Aluno reprovado")
    elif media > 5 and media < 7:
        print("Aluno em recuperação")
    elif media >= 7:
        print("Aluno aprovado")
    nota = []
    nota.append(nota1)
    nota.append(nota2)
    nota.append(nota3)
    alunos[nome] = nota

print(alunos)