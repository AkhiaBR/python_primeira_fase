#EXERCICIO7
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Diigte o valor de seu peso: "))
altura = float(input("Digite o valor da sua altura: "))
imc = (peso/(altura*altura))
print(nome, "seu IMC é: ", imc)