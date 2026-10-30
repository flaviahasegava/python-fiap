import os
os.system("cls")

''' 
Considere o valor dos vetores abaixo para fazer os próximos exercícios: 
  v1 = [41, 72, 39, 4, 35] 
  v2 = [0, 0, 0, 0, 0] 

7. Fazer um programa que copie os elementos invertidos do vetor v1 em v2, ou seja, o primeiro elemento de v1 será o último de v2. 
  >> [41, 72, 39, 4, 35] 
  >> [35, 4, 39, 72, 41] 
'''

# Cria uma lista com 5 elementos v1 e v2
v1 = [41, 72, 39, 4, 35] 
v2 = [0, 0, 0, 0, 0]

# Laço de repetição
for i in range(0, 5, 1):
  
  # Copia os elementos do v1 para o v2 em ordem invertida usando o cálculo de "4 - i" para ir diminuindo o valor do índice que será guardado
  v2[i] = v1[4 - i]

# Exibe o vetor 1 e vetor 2 ao contrário
print(f'''
{v1}
{v2}
''')