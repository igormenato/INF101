def calcular_salario():
    numero_funcionario = input("Digite o número do funcionário: ")
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    valor_por_hora = float(input("Digite o valor que recebe por hora: "))
    numero_filhos_menores_14 = int(
        input("Digite o número de filhos com idade menor de 14 anos: ")
    )

    salario_base = horas_trabalhadas * valor_por_hora
    adicional_por_filhos = salario_base * 0.10 * numero_filhos_menores_14
    salario_total = salario_base + adicional_por_filhos

    print(f"Funcionário {numero_funcionario} tem um salário de R$ {salario_total:.2f}")


if __name__ == "__main__":
    calcular_salario()
