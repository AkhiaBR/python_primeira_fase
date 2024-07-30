contador = 0
soma = 0

for contador in range(1, 11):
    numero = int(input("Digite um número: "))
    if (numero < 0):
        break 
    soma+=1
    resultado = soma*numero

print("Soma dos números: ", resultado)
