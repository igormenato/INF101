def verificar_letra(letra):
    vogais = {
        "A": "Vogal maiúscula",
        "E": "Vogal maiúscula",
        "I": "Vogal maiúscula",
        "O": "Vogal maiúscula",
        "U": "Vogal maiúscula",
        "a": "Vogal minúscula",
        "e": "Vogal minúscula",
        "i": "Vogal minúscula",
        "o": "Vogal minúscula",
        "u": "Vogal minúscula",
    }

    if letra in vogais:
        return vogais[letra]
    else:
        return "Consoante"


def main():
    letra = input("Digite uma letra: ")
    resultado = verificar_letra(letra)
    print(resultado)


if __name__ == "__main__":
    main()
