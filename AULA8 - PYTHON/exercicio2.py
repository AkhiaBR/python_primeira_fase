#exercicio2

contador = 0
contadorc = 0
contadort = 0
contadorf = 0

while contador < 50:
    contador += 1
    nome = str(input("Digite seu nome: "))
    cidade = str(input("Digite a sigla da cidade que você mora (Criciúma = C, Tubarão = T, Florianopolis = F): ")).upper()

    if cidade == "C":
        contadorc += 1
    elif cidade == "T":
        contadort += 1
    elif cidade == "F":
        contadorf += 1

print("O número de pessoas que moram em Criciúma, Tubarão e Florianópolis é, respectivamente: ", contadorc, ",", contadort, ",", contadorf)
