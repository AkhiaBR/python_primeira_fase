#IF04

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if (idade<3):
    print("Você é um bebê")
elif (idade>=4 and idade<=11):
    print("Você é uma criança")
elif (idade>=12 and idade<=17):
    print("Você é um adolescente")
elif (idade>=18 and idade<=60):
    print("Você é um adulto")
elif (idade>=61):
    print("Você é um idoso")