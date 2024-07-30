#practice2

quantidade = int(input("Digite o número de notas para a obtenção da média: "))
contador = 0
nota = 0
soma = 0
media = 0

while contador < quantidade:
    contador += 1
    nota = float(input("Digite sua nota: "))
    soma += nota

media = soma/quantidade

print("Sua média de notas é: ", media)

    
