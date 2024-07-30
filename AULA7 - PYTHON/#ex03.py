#ex03

contador = 1
maior = 0
menor = 999999999

for contador in range(1,11):
    numero = int(input("Digite um número: "))
    
    if (numero > maior):
        maior = numero
    
    if (numero < menor):
        menor = numero

print("Maior número lido: ", maior)
print("Menor valor lido: ", menor)