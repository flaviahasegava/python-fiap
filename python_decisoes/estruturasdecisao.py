import os
os.system("cls")

# Problema: Numa festa, os presentes do sexo masculino pagam a entrada 
# Informe se a pessoa paga ou não a entrada

# - Digitar o sexo do usuário
sexo = input("[M]asculino ou [F]eminino? ")
# - Se for do sexo masculino
if sexo == 'm':
    # - Exibe a mensagem da cobrança
    print("Será efetuada a cobrança")

# Exercício:
# Dado um número pelo usuário, exibir o seu positivo
# ENTRADA: 56           SAÍDA: 56
# ENTRADA: -33          SAÍDA: 33

os.system("cls")
# - Digitar um número
numero = float(input("Digite um número: "))
if numero > 0:
    n = n * -1
    # - Exibe o número positivo
    print(numero)