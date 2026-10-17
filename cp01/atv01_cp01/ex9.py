"""
PROBLEMA: 
Dado um N° e um múltiplo, mostre o múltiplo anterior e posterior
Número: 15
Múltiplo: 6

Anterior: 12
Próximo: 18
"""

# - Digitar um número e um múltiplo
num = int(input("Digite um número: "))
multiplo = int(input("Digite um múltiplo: "))
# - Calcular o múltiplo anterior e posterior do número
mult_anterior = (num // multiplo) * multiplo
mult_posterior = mult_anterior + multiplo
# - Exibir o resultado
print("Múltiplo anterior: ", mult_anterior)
print("Múltiplo posterior: ", mult_posterior)