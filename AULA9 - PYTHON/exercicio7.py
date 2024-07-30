#exercicio7

lista = []
contador = 0

while contador < 5:
    contador += 1
    valor = int(input("Digite um número: "))
    lista.append(valor)

listaSum = sum(lista)

print("A soma dos números é: ", listaSum)
