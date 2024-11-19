def verificar_dia_semana(numero):
    match numero:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-feira"
        case 3:
            return "Terça-feira"
        case 4:
            return "Quarta-feira"
        case 5:
            return "Quinta-feira"
        case 6:
            return "Sexta-feira"
        case 7:
            return "Sábado"
        case _:
            return "Número inválido"


def main():
    try:
        numero = int(input("Digite um número (1-7): "))
        dia = verificar_dia_semana(numero)
        print(f"O dia correspondente é: {dia}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")


if __name__ == "__main__":
    main()
