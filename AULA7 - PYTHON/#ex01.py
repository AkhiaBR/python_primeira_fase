#ex01

num = int(input("Digite o número desejado para a criação da tabuada: "))
 
for cont in range(1,11):
    result = num*cont
    print(num, "X", cont, "=", result)