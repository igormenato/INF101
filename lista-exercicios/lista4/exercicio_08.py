def calcular_pa(n, primeiro_termo, razao):
    termos = []
    soma = 0

    for i in range(n):
        termo = primeiro_termo + i * razao
        termos.append(termo)
        soma += termo

    return termos, soma


def main():
    n = int(input("Digite o número de elementos da PA: "))
    primeiro_termo = int(input("Digite o primeiro termo da PA: "))
    razao = int(input("Digite a razão da PA: "))

    termos, soma = calcular_pa(n, primeiro_termo, razao)

    print("Termos da PA:", termos)
    print("Soma dos elementos:", soma)


if __name__ == "__main__":
    main()
