"""
7. Dado um valor, calcular e exibir o próximo múltiplo de 5.
Entrada: 12
Saída: O próximo múltiplo de 5 após 12 é 15
"""

valor = int(input("Digite um valor: "))
multiplo = valor + (5 - (valor % 5))
print("O próximo múltiplo de", valor, "é", multiplo)
