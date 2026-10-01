import os
os.system("cls")

# - Digitar o valor recebido por hora trabalhada
valor = float(input("Qual o valor recebido por hora trabalhada? "))
# - Digitar a quantidade de horas trabalhadas durante o mês
horas = int(input("Qual a quantidade de horas trabalhadas? "))
# - Calcular o salário total do funcionário
salario = valor * horas
# - Exibir o resultado
print(f"O seu salário é de R$ {salario:.2f}")