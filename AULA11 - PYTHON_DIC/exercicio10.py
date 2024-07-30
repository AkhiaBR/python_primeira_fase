#exercicio10

estados = {"Acre" : "Capital Rio Branco",  "Alagoas" :  "Capital Maceió", 
                    "Amazonas": "Capital Manaus",  "Bahia" : "Capital Salvador", 
                    "Distrito Federal" : "Capital Brasília",  "Santa Catarina" : "Capital Florianópolis", 
                    "Rio Grande do Sul" : "Capital Porto Alegre",
                    "Paraná" : "Capital Curitiba", "São Paulo" : "Capital São Paulo",
                    "Minas Gerais" : "Cuiabá", "Rio de Janeiro" : "Rio de Janeiro",
                    "Tocantins": "Capital Palmas"}

print(estados)
print("--------------")
x = str(input("Digite o nome do estado que deseja cadastrar: "))
y = str(input("Qual a capital do estado?: "))
estados.update({x:y})
estados["Mina Gerais"] = "Belo Horizonte"
print(estados)

if "Distrito Federal" in (estados):
    print("Distrito Federal está em estado")
else:
    print("Distrito Federal não está em estados")
