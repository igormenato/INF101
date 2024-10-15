def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_aprovacao(presencas, media):
    if media > 6 and presencas >= 20:
        return "APROVADO"
    elif 5 <= media < 6 and presencas >= 20:
        return "DEPENDÊNCIA"
    else:
        return "REPROVADO"


def ler_notas():
    notas = []
    for i in range(4):
        nota = float(input(f"Informe a nota {i+1}: "))
        notas.append(nota)
    return notas


def ler_presencas():
    presencas = int(input("Informe o número de presenças: "))
    return presencas


def main():
    notas = ler_notas()
    presencas = ler_presencas()
    media = calcular_media(notas)
    resultado = verificar_aprovacao(presencas, media)
    print(resultado)
