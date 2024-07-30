#exercicio8

lista = []
contador = 0

while contador < 10:
    contador += 1
    idade = int(input("Digite sua idade: "))
    lista.append(idade)

lista.sort(reverse=False)

print("As idades em ordem crescente serão de: ", lista)