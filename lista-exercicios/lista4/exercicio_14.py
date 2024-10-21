def calcular_tabuada(numero):
    contador = 1
    while contador <= 10:
        resultado = numero * contador
        print(f"{numero} x {contador} = {resultado}")
        contador += 1


def main():
    numero = int(input("Digite um número: "))
    calcular_tabuada(numero)


if __name__ == "__main__":
    main()
