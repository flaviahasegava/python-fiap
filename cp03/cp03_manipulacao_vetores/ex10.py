import os
os.system("cls")

'''
Considere o valor dos vetores abaixo para fazer os próximos exercícios: 
  v1 = [41, 72, 39, 4, 35] 
  v2 = [0, 0, 0, 0, 0] 

10. Fazer um programa que retorne o elemento de maior valor do vetor. 
  x = maior_elemento(v1) 
  >> x valerá 72 
'''

# Cria função para achar o maior elemento do vetor
def maior_elemento(v1):

  # Guarda o valor do índice 0 na variável maior
  maior = v1[0]

  # Laço de repetição
  for i in range(0, 5, 1):

    # Verifica se os valores de cada índice é maior que a variável "maior"
    if v1[i] > maior:
      
      # Caso o elemento do índice seja maior, ele é guardado na variável
      maior = v1[i]

  # Retorna o resultado do maior valor do elemento
  return maior

# Cria uma lista com 5 elementos
v1 = [41, 72, 39, 4, 35]

# Guarda o maior elemento na variável "x"
x = maior_elemento(v1)

# Exibe o resultado do maior elemento
print(f"O maior elemento do vetor é {x}")