import os
os.system("cls")

''' 
Considere o vetor v = [45, -89, 32, -12, 33]: 

2. Fazer um programa que exiba os elementos cujos índices sejam pares. 
    >> -32 -12 
'''

# Cria uma lista com 5 elementos
v = [45, -89, 32, -12, 33]

# Laço de repetição do índice
for i in range(0, 5, 1): 
    # Guarda o valor do índice (0 a 4) na variável 
    par = v[i]

    # Verifica se a variável "par" que foi guardada o índice é par
    if par % 2 == 0:
        # Mostra os índices pares
        print(par, end=" ")