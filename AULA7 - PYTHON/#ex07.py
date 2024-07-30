#ex07

contador = 0
soma = 0

for contador in range(1,11):
    contador+=1
    numero = int(input("Digite um número: "))
    soma = soma+numero

media = soma/soma.len()

print("A soma dos dez números é: ", soma)
print("A média dos números é: ", media)