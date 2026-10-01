"""
PROBLEMA: 
Dados os valores a, b e c, calcular o valor de delta
Fórmula: delta = b**2 - 4 * a * c
Entrada: a = 1, b = 5, c = 6
Saída: O valor de delta é 1
"""
# - Digitar o primeiro número 
a = float(input("Digite o valor de a: "))
# - Digitar o segundo número
b = float(input("Digite o valor de b: "))
# - Digitar o terceiro número 
c = float(input("Digite o valor de c: "))
# - Calcular delta
delta = b**2 - 4 * a * c
# - Exibir o resultado 
print("O valor de delta é ", delta)
