import os
os.system("cls")

''' 
Considere o vetor v = [45, -89, 32, -12, 33]: 

5. Fazer um programa que peça um valor ao usuário e conte quanto dele há no vetor.
  Valor: 32 
  >> Há um elemento 32 no vetor
'''

# Cria uma lista com 5 elementos
v = [45, -89, 32, -12, 33]

# Pede o valor ao usuário
numero = int(input("Valor: "))

# Cria a variável do contador
qtd = 0

# Laço de repetição
for i in range(0, 5, 1):

  # Verifica se o vetor de cada índice é igual ao valor digitado pelo usuário
  if v[i] == numero:
    
    # Conta a quantidade de dados iguais ao valor do usuário
    qtd = qtd + 1

# Exibe o resultado da quantidade de elementos iguais ao número digitado
print(f"Há {qtd} elemento {numero} no vetor")