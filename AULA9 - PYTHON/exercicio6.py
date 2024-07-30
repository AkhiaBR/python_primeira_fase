#exercicio6

listamedia = []
contador = 0
media = 0

while contador < 10:
    contador += 1
    valor1 = int(input("Digite sua primeira nota: "))
    valor2 = int(input("Digite sua segunda nota: "))
    media = (valor1+valor2)/2
    listamedia.append(media)

print("A média de cada aluno, respectivamente é: ", listamedia)