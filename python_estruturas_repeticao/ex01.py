import os
os.system("cls")

'''
Exercícios
1. Dados dois números pelo usuário, exibe o intervalo FECHADO.
ENTRADA: 3 9       SAÍDA: 3 4 5 6 7 8 9

2. Dados dois números pelo usuário, exibe o intervalo ABERTO.
ENTRADA: 3 9       SAÍDA: 4 5 6 7 8
'''

# EXERCÍCIO 01
# Pedir dois números
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

for contagem in range(num1, num2 + 1, 1):
    print(contagem, end = " ")