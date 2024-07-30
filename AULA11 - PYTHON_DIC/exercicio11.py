#exercicio11

times = {1: "Criciuma",  2: "Avai",  3: "Marcilio Dias", 4: "Joinville", 
        5: "Figueirense",  6: "Chapecoense",  7: "Brusque", 8: "Metropolitano",
        9: "Hercílio Luz", 10: "Inter de Lages" }
print(times)

x = int(input("Digite o número do time que deseja adicionar: "))
y = str(input("Digite o nome do time: "))
times.update({x:y})

if "Joinville" in (times):
    print("Joinville está presente nos times")
else:
    print("Joiville não está presente nos times")

del times[2]

print(times)
