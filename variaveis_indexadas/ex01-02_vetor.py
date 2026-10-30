import os
os.system("cls")

# EXERCÍCIOS DE VETOR
'''
1. Crie um vetor de inteiro com 5 posições. Peça para o usuário digitar valores em todas as posições, depois exiba o conteúdo posição a posição.
2. Depois de digitado os valores no vetor, calcular a somatória dos dados e a média dos elementos do vetor.
'''

#    0  1  2  3  4
v = [0, 0, 0, 0, 0]

# v[0] = int(input("Valor 1: "))
# v[1] = int(input("Valor 2: "))
# v[2] = int(input("Valor 3: "))
# v[3] = int(input("Valor 4: "))
# v[4] = int(input("Valor 5: "))
# print(v)

# Outra forma melhor de fazer

soma = 0

for i in range(0, 5, 1):
    v[i] = int(input(f"v[{i}]: "))
    soma = soma + v[i]

for i in range(0, 5, 1):
    print(f"v[{i}] = {v[i]}")

# Calcula a média
media = soma / 5

# Exibe o resultado
print(f'''
RESULTADO FINAL
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Soma:................ {soma:.2f}
Média:............... {media:.2f}
Vetor: {v}
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
''')