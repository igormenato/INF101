def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media


def verificar_situacao(media):
    if media >= 6:
        return "Aprovado"
    elif 5 <= media < 6:
        return "Dependência"
    else:
        return "Reprovado"


def main():
    print("Digite as 4 notas do aluno em Cálculo:")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    media = calcular_media(nota1, nota2, nota3, nota4)

    situacao = verificar_situacao(media)

    print(f"\nMédia do aluno: {media:.2f}")
    print(f"Situação do aluno: {situacao}")


if __name__ == "__main__":
    main()
