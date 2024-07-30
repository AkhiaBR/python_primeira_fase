#IF02

nome = str(input("Digite sue nome: "))
print("Cursos disponíveis: ")
print("ADM -> Administração")
print("DIR -> Direito")
print("CEX -> Comércio Exterior")
curso = str(input("Digite a sigla do seu curso: "))

if (curso == "ADM" or "adm"):
    print(nome ,"seu curso é administração.")
elif (curso == "DIR" or "dir"):
    print(nome ,"seu curso é direito")
elif (curso == "CEX" or "cex"):
    print(nome ,"seu curso é comércio exterior")
