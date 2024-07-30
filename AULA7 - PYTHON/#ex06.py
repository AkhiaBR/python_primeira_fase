numero = int(input("Digite um número inteiro: "))
for n in range(2,numero):
    if (numero % n == 0):
        print("NÃO É um número primo")
        break
    else:
        print("É um número primo")
        break