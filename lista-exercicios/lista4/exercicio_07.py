def calcular_pa(n, primeiro_termo, razao):
    termos = []
    soma = 0
    i = 0

    while i < n:
        termo = primeiro_termo + i * razao
        termos.append(termo)
        soma += termo
        i += 1

    return termos, soma


def main():
    n = int(input("Digite o número de elementos da PA: "))
    primeiro_termo = float(input("Digite o primeiro termo da PA: "))
    razao = float(input("Digite a razão da PA: "))

    termos, soma = calcular_pa(n, primeiro_termo, razao)

    print("Termos da PA:", termos)
    print("Soma dos elementos:", soma)


if __name__ == "__main__":
    main()
