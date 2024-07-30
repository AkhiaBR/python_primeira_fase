#exercicio10

nome = str(input("Digite o seu nome: "))
senha = str(input("Digite a sua senha: "))

while senha == nome:
    print("Sua senha não pode ser igual ao seu nome, digite uma nova senha: ")
    senha = str(input("Digite sua nova senha: "))

print("Sua nova senha é: ", senha)