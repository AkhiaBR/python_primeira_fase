#exercicio13

produtos = {}
contador = True

while(contador == True):
    print("---------------------")
    print("1- CADASTRAR Produto/Preço")
    print("2- PESQUISAR")
    print("3- ALTERAR Produto Preço")
    print("4- EXCLUIR Produto Preço")
    print("5- INCLUIR NOVO Produto")
    print("6- SAIR")
    print("---------------------")
    selecao = int(input("Digite a opção de acordo com o número referente: "))
    if(selecao == 1):
        x = str(input("Digite o nome do produto: "))
        y = float(input("Digite o valor desse produto: "))
        produtos.update({x:y})
    elif(selecao == 2):
        sorted(produtos)
        print(produtos)
    elif(selecao == 3):
        x = str(input("Digite o nome do produto a ser alterado: "))
        produtos.pop(x)
        xAlt = str(input("Digite o novo nome do produto: "))
        yAlt = float(input("Digite o valor do produto: "))
        produtos.update({xAlt:yAlt})
    elif(selecao == 4):
        remove = str(input("Digite o produto que deseeja remover: "))
        produtos.pop(remove)
    elif(selecao == 5):
        x = str(input("Digite o nome do novo produto: "))
        produtos.update({x:0})
    elif(selecao == 6):
        x = str(input("Deseja encerrar o programa? Sim (S) ou não (N): ")).upper()
        if(x == "S"):
            contador = False
        elif(x == "N"):
            contador == True