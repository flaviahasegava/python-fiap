import os
os.system("cls")

'''
2. Par ou ímpar 
Solicite um número inteiro. Utilize uma decisão para informar se ele é par ou ímpar.
'''

# Solicitar o número inteiro
numero = int(input("Digite um número inteiro: "))
# Verificar se o número é par ou ímpar
if numero > 0:  
    print("O número é par.")
else:
    print("O número é zero ou negativo.")