#exercicio4

lista = []
contador = 0
vogal = 0
con = 0

while contador < 3:
    contador += 1
    valor = str(input("Digite alguma letra: ")).lower()
    lista.append(valor)

    if valor == "a" or valor == "e" or valor == "i" or valor == "o" or valor == "u":
        vogal += 1
    else :
        con += 1

print("Palavras obtidas: ")
print("Número de vogais: ", vogal, ", número de consoantes: ", con)