import os
os.system("cls")

'''
1. Número positivo ou não positivo 
Solicite um número inteiro. Informe se o número é positivo. Caso contrário, informe que ele é zero ou 
negativo. 
ENTRADA: -4
SAÍDA: O número é zero ou negativo

'''

# Solicitar o número inteiro
numero = int(input("Digite um número inteiro: "))
# Verificar se o número é par ou ímpar
if numero > 0:  
    print("O número é par.")
else:
    print("O número é zero ou negativo.")