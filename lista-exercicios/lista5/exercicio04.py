TAMANHO_MAXIMO = 20


def contar_ocorrencias(vetor, numero):
    return vetor.count(numero)


def main():
    try:
        entrada = input("Digite os números do vetor separados por espaço: ")
        vetor = [int(x) for x in entrada.split()]

        if len(vetor) > TAMANHO_MAXIMO:
            print(f"Erro: O vetor não pode ter mais que {TAMANHO_MAXIMO} elementos")
            return

        numero = int(input("Digite o número que deseja procurar: "))

        quantidade = contar_ocorrencias(vetor, numero)

        print(f"O número {numero} aparece {quantidade} vezes no vetor.")

    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.")


if __name__ == "__main__":
    main()
