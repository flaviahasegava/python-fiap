''' 
Exercício 01:
1. Dado o valor inicial e o final pelo usuário, exiba os números do intervalo FECHADO.
ENTRADA: 4 9       SAÍDA: 4 5 6 7 8 9
    v2.0 Exiba no formato matemático:
    # ENTRADA: 4 9   SAÍDA: [4, 5, 6, 7, 8, 9]
'''

# EXERCÍCIO 01
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print("[", end = "")

for contagem in range(num1, num2 + 1, 1):
    print(contagem, end = " ")

    if num2 < num1:
        print(end = ", ")

print("]", end = "")