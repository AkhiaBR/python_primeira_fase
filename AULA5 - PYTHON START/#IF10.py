#IF10

valor1 = float(input("Digite o primeiro valor: "))
op = str(input("Digite a sigla da operação desejada(+, -, * e /): "))
valor2 = float(input("Digite o segundo valor: "))

if (op == "+"):
    print("O resultado da operação é: ", valor1+valor2)
elif (op == "-"):
    print("O resultado da operação é: ", valor1-valor2)
elif (op == "*"):
    print("O resultado da operação é: ", valor1*valor2)
elif (op == "/"):
    print("O resultado da operação é: ", valor1/valor2)