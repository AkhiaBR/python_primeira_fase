#exercicio04

livros = {}

for i in range(5):
    nome = str(input("Digite o nome do livro: "))
    autor = str(input("Digite o nome de seu respectivo autor: "))
    livros[nome] = autor

print(livros)