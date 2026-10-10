'''
2. Dado o valor inicial e o final pelo usuário, exiba os números do intervalo ABERTO.
ENTRADA: 4 9       SAÍDA: 5 6 7 8 
    v2.0 Exiba no formato matemático:
    ENTRADA: 4    9   SAÍDA: ]5, 6, 7, 8[
'''

# EXERCÍCIO 02
num1 = int(input('Digite o valor inicial: '))
num2 = int(input('Digite o valor final: '))

print("]", end = "")

for contagem in range(num1, num2 + 1, 1):
    print(contagem, end = " ")

    if num2 < num1:
        print(end = ", ")
        
print("[", end = "")

