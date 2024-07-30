#exercicio9

lista = []
contador = 0

while contador < 10:
    contador += 1
    numero = int(input("Digite um número: "))
    lista.append(numero)

maior = max(lista)
menor = min(lista)

print("***Os números digitados foram: ", lista)
print("***O maior número da lista foi: ", maior, ", o menor número da lista foi: ", menor)
