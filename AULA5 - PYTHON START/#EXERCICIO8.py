#EXERCICIO9

nome = str(input("Digite seu nome: "))
carga = int(input("Digite a sua carga horaria: "))
valor = float(input("Digite o valor ganho por hora: "))
bruto = (carga*valor)
final = (bruto-(bruto*2/100))
print(nome, "o salário final com desconto de INSS é de: ", final)