def trocar_valores(vA, vB):
    return vB, vA


def main():
    vA = float(input("Digite o valor de vA: "))
    vB = float(input("Digite o valor de vB: "))

    vA, vB = trocar_valores(vA, vB)

    print(f"Após a troca, vA = {vA} e vB = {vB}")


if __name__ == "__main__":
    main()
