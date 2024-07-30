#exercicio11

listaMedia = []
listaApr = []
listaRep = []
contador = 0
media = 0

while contador < 2:
    contador += 1
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    nota3 = float(input("Digite sua terceira nota: "))
    nota4 = float(input("Digite sua quarta nota: "))
    media = (nota1+nota2+nota3+nota4)/4
    listaMedia.append(media)

    if media >= 7 and media < 10:
        listaApr.append(media)
    else:
        listaRep.append(media)

print("***Lista de médias dos alunos: ", listaMedia)
print("***Lista de alunos aprovados: ", listaApr)
print("***Lista de alunos reprovados: ", listaRep)