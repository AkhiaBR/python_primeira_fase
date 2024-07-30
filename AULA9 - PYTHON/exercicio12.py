#exercicio12

vetor1 = []
vetor2 = []
vetorSoma = []
contador = 0

while contador < 5:
    contador += 1
    numero = int(input("Digite um número para o vetor 1: "))
    numero2 = int(input("Digite um número para o vetor 2: "))
    vetor1.append(numero)
    vetor2.append(numero2)
    vetorSoma = vetor1+vetor2

print("***Os números do vetor 1 são: ", vetor1)
print("***Os números do vetor 2 são: ", vetor2)
print("***Os dois vetores em conjunto formam: ", vetorSoma)
