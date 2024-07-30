#exercicio12

atletas = { "Cristiano Ronaldo" : "Futebol", "LeBron James" : "Basquete",
                    "Lionel Messi" : "Futebol", "Neymar" : "Futebol",
                    "Conor McGregor" : "MMA", "Roger Federer" : "Tênis",
                     "Rafael Nadal" : "Tênis",  "Stephen Curry" : "Basquete",
                     "Tiger Woods" : "Golfe",  "Kevin Durant" : "Basquete",
                      "Lewis Hamilton" : "Fórmula 1", "Sun Yang" : "Natação" }

print(atletas)
print("---------------")

x = str(input("Digite o nome do novo atleta: "))
y = str(input("De qual modalidade esportiva ele faz parte?: "))
atletas.update({x:y})

del atletas["Tiger Woods"]

if "Roger Federer" in (atletas):
    print("O atleta Roger Federer está presente no dicionário")
else:
    print("O atleta Roger Federer não está presente no dicionário atletas")

print("--------------")
print(atletas)