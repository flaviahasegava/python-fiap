import os
os.system("cls")

''' 
Considere o vetor v = [45, -89, 32, -12, 33]: 

4. Fazer um programa que ordene os elementos do vetor. 
  >> -89 -12 32 33 45 
'''

# Cria uma lista com 5 elementos
v = [45, -89, 32, -12, 33]

# Laço de repetição
for i in range(0, 5, 1):

  for j in range(0, 4, 1):

    # Verifica se o elemento da esquerda é maior que o da direita
    if v[j] > v[j + 1]:
      # Guarda temporário o valor da esquerda
      guardar_num = v[j]
      # Copia o menor valor da direita para a posição da esquerda
      v[j] = v[j + 1]
      # Coloca o valor que estava no "guardar_num" na posição da direita
      v[j + 1] = guardar_num

# Laço de repetição
for i in range(0, 5, 1):
  # Exibe o resultado em ordem crescente dos elementos
  print(v[i], end=" ")