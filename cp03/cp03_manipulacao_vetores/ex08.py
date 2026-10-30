import os
os.system("cls")

''' 
Considere o valor dos vetores abaixo para fazer os próximos exercícios: 
    v1 = [41, 72, 39, 4, 35] 
    v2 = [0, 0, 0, 0, 0] 

8. Fazer programa que ordene em ordem decrescente o vetor 
    >> [72, 41, 39, 35, 4] 
'''

# Cria função para ordenar em ordem decrescente
def ordem_decrescente(v1):
    
    # Laço de repetição
    for i in range(0, 5, 1):

        for j in range(0, 4, 1):
            
            # Verifica se o elemento atual for menor que o próximo e troca as posições
            if v1[j] < v1[j + 1]:
                guardar_num = v1[j]
                v1[j] = v1[j + 1]
                v1[j + 1] = guardar_num

    # Retorna em ordem decrescente os elementos
    return v1

# Cria uma lista com 5 elementos
v1 = [41, 72, 39, 4, 35]

# Ativa a função
ordem_decrescente(v1)

# Exibe o resultado dos elementos em ordem decrescente
print(v1)