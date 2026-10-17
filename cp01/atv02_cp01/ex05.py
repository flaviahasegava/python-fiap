import os
os.system("cls")

'''
5. Número dentro de um intervalo 
Solicite um número inteiro e informe se ele está entre 10 e 20, inclusive. Use o operador lógico and.
'''

# Solicitar um número
numero = int(input("Digite um número: "))
# Verificar se o número está entre 10 e 20
if numero >= 10 and numero <= 20:
    print("O número está entre 10 e 20.")
else:
    print("O número não está entre 10 e 20.")