#exercicio5

lista = []
listaPar = []
listaIm = []
contador = 0

while contador < 20:
    contador += 1
    valor = int(input("Digite um número: "))
    lista.append(valor)

    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaIm.append(valor)

print("Números digitados: ", lista)
print("Números pares: ", listaPar)
print("Números ímpares: ", listaIm)