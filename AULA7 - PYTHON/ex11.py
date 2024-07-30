#ex11

nome = str(input("Digite seu nome: "))

while nome.len() < 3:
    print("Você digitou seu nome errado, faça de novo: ")
    nome = str(input("Digite seu nome: "))