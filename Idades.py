with open("Idades.txt", "r") as info:
    linhas = info.read().splitlines()

    row_data0 = linhas[0].split(",")
    row_data1 = linhas[1].split(",")
    row_data2 = linhas[2].split(",")

    print("{0} tem {1} anos de idade e é {2}".format(row_data0[0], row_data0[1], row_data0[2]) + "\n")
    print("{0} tem {1} anos de idade e é {2}".format(row_data1[0], row_data1[1], row_data1[2]) + "\n")
    print("{0} tem {1} anos de idade e é {2}".format(row_data2[0], row_data2[1], row_data2[2]) + "\n")
