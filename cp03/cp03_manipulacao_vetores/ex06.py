import os
os.system("cls")

''' 
Considere o valor dos vetores abaixo para fazer os próximos exercícios: 
  v1 = [41, 72, 39, 4, 35] 
  v2 = [0, 0, 0, 0, 0] 

6. Fazer programa que copie os elementos do vetor v1 em v2. 
  >> 41, 72, 39, 4, 35 
  >> 45 33 
'''

# Cria uma lista com 5 elementos v1 e v2
v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

# Laço de repetição
for i in range(0, 5, 1):
  # Guarda o valor de v1 em v2
  v2[i] = v1[i]

  # Verifica se o valor de "i" é igual a 4 para printar o último índice de v2 e não ter vírgula no final
  if i == 4:
    print(v2[i])

  # Caso o "i" não seja igual a 4, continua printando os elementos de v2 separados por vírgula
  else:
    print(v2[i], end=", ")