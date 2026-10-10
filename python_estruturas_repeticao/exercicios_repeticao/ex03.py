'''
3. Dado um numero pelo usuário, exibir os seus 10 primeiros múltiplos.
    ENTRADA: 5        SAÍDA: 5 10 15 20 25 30 35 40 45 50
'''

# EXERCÍCIO 03
num = int(input('Digite um número: '))

for volta in range(1, 11, 1):
    mult = num * volta
    print(mult, end = " ")