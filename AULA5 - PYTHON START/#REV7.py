#REV7

dia = int(input("Insira um número de 1 a 7: "))

if(dia == 1):
    print("O dia da semana é domingo")
elif(dia == 2):
    print("O dia da semana é segunda-feira")
elif(dia == 3):
    print("O dia da semana é terça-feira")
elif(dia == 4):
    print("O dia da semana é quarta-feira")
elif(dia == 5):
    print("O dia da semana é quinta-feira")
elif(dia == 6):
    print("O dia da semana é sexta-feira")
elif(dia == 7):
    print("O dia da semana é sábado")
elif(dia > 7 or dia < 1):
    print("Valor inserido errado")