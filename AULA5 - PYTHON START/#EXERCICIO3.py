#EXERCICIO3

nome = str(input("Digite seu nome: "))
curso = str(input("Digite seu curso: "))
dis = str(input("Digite sua disciplina: "))
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = ((nota1+nota2+nota3)/3)
print(nome, "do curso", curso, "disciplina: ", dis, "sua média é: ", media)