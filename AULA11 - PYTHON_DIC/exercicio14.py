#exercicio14

padaria = {}
status = True

while(status == True):
    print("-------------------------")
    print("1- CADASTRAR")
    print("2- PESQUISAR")
    print("3- ALTERAR")
    print("4- EXCLUIR")
    print("5- INCLUIR")
    print("6- SAIR")
    print("-------------------------")
    escolha = int(input("Digite o número referente à escolha das opções: "))
    if(escolha == 1):
        produto = []
        x = int(input("Qual o código do produto a ser cadastrado: "))
        nome = str(input("Digite o nome do produto: "))
        valor = float(input("Digite o preço desse produto: "))
        quantidade = int(input("Digite a quantidade de estoque desse produto: "))
        produto.append(nome)
        produto.append(valor)
        produto.append(quantidade)
        padaria[x] = produto
    elif(escolha == 2):
        sorted(padaria)
        print(padaria)
    