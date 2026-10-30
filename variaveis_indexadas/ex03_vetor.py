import os
os.system("cls")

# EXERCÍCIOS DE VETOR
'''
3. Faça um programa que analise um vetor de inteiros com 10 posições e exiba o de menor valor.
'''

v = [32, 10, 30, 90, 80, 20, 320, 50, 43, 7]

menor = v[0]

for i in range(1, 10, 1):
    if v[i] < menor:
        menor = v[i] 

print(f'''
RESULTADO FINAL
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Menor número:............. {menor}
Vetor: {v}
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
''')

# Outra forma pedindo o número do vetor para o usuário

v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    v[i] = int(input(f"v[{i + 1}]: "))

menor = v[0]

for i in range(1, 10):
    if v[i] < menor:
        menor = v[i] 

print(f'''
RESULTADO FINAL
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Menor número:............. {menor}
Vetor: {v}
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
''')