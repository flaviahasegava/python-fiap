import os
os.system("cls")

'''
12. Número fora do intervalo 
Solicite um número inteiro. Informe se ele está fora do intervalo de 1 a 100. Utilize o operador lógico or.
'''

#
numero = int(input("Informe um número inteiro: "))

if numero >= 1 or numero <= 100:
    print("O número está dentro do intervalo de 1 a 100.")
else:
    print("O número está fora do intervalo de 1 a 100.")