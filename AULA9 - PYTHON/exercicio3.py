#exercicio3

lista = []
contador = 0

while contador < 4:
    contador += 1
    nota = float(input("Digite uma nota: "))
    lista.append(nota)

soma = sum(lista)

print("Suas notas foram: ", lista)
print("Sua média foi: ", soma/contador)