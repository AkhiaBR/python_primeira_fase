#exercicio10

lista = []
contador = 0

while contador < 10:
    contador += 1
    numero = int(input("Digite um número: "))
    lista.append(numero)

lista.sort(reverse=True)

print("Os números digitados em ordem decrescente são: ", lista)