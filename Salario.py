def calcular_reajuste(salario):

    if salario <= 280:
        aumento_percentual = 20

    elif salario <= 700:
        aumento_percentual = 15

    elif salario <= 1500:
        aumento_percentual = 10

    else:
        aumento_percentual = 5

    aumento = salario * aumento_percentual / 100

    novo_salario = salario + aumento

    aumento_real = aumento - (aumento * 3.8 / 100)

    return aumento_percentual, aumento, novo_salario, aumento_real

salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

aumento_percentual, aumento, novo_salario, aumento_real = calcular_reajuste(salario_atual)

print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {aumento_percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"novo salário após o aumento: R$ {novo_salario:.2f}")
print(f"Valor do aumento real, descontado a inflação (3,8): R$ {aumento_real:.2f}")