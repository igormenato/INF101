def imprimir_tabuada():
    for multiplicador in range(1, 11):
        for numero in range(1, 6):
            resultado = numero * multiplicador
            print(f"{numero} x {multiplicador} = {resultado}", end="\t")
        print()


def main():
    imprimir_tabuada()


if __name__ == "__main__":
    main()
