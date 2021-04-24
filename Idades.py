with open("Idades.txt", "r") as info:
    linhas = info.read().splitlines()
    
    for i in range(len(linhas)):
        por_linha = linhas[i].split(",")

        print(f"{por_linha[0]} tem {por_linha[1]} anos de idade e é {por_linha[2]}" + "\n")

