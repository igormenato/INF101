def calcular_tabuada():
    for i in range(1, 6):
        for j in range(1, 11):
            print("{:2d} x {:2d} = {:2d}".format(i, j, i * j), end="\t")
        print()


calcular_tabuada()
