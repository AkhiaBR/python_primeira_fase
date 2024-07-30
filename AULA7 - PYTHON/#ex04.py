#ex04

fatorial = 1
contador = 1
numero = int(input("Digite um número: "))

for contador in range(1,numero+1):
    fatorial = fatorial*contador

print("Fatorial do número: ",numero,"=",fatorial)