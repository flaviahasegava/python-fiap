'''
4. Dado um numero pelo usuário e um multiplicador M, exibir os seus M primeiros múltiplos.
    ENTRADA: 5  6     SAÍDA: 5 10 15 20 25 30 
'''

# EXERCÍCIO 04
num = int(input("Digite um número: "))
mult = int(input("Digite um multiplicador: "))

for volta in range(num, num * mult + 1, num):
    print(volta, end = " ")