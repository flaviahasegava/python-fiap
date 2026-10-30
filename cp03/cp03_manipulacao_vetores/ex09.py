import os
os.system("cls")

''' 
Considere o valor dos vetores abaixo para fazer os próximos exercícios: 
    v1 = [41, 72, 39, 4, 35] 
    v2 = [0, 0, 0, 0, 0] 

9. Fazer um programa que conte quanto elementos estão acima da média 
    x = conta_acima_media(v1) 
    >> x valerá 3 
'''

# Cria função para contar quantos elementos estão acima da média
def conta_acima_media(v1):

    # Cria as variáveis do contador
    soma = 0
    qtd = 0
    
    # Laço de repetição
    for i in range(0, 5, 1):

        # Calcula a soma dos elementos e o total de elementos
        soma = soma + v1[i]
        qtd = qtd + 1

    # Calcula a média dos elementos    
    media = soma / qtd
    
    # Cria a variável de contar os elementos maiores que a média
    contador = 0

    # Laço de repetição
    for i in range(0, 5, 1):

        # Verifica cada índice do vetor se está acima da média
        if v1[i] > media:
            # Conta os que estão acima da média
            contador = contador + 1

    # Retorna a quantidade de elementos acima da média        
    return contador

# Cria uma lista de 5 elementos 
v1 = [41, 72, 39, 4, 35]

# Guarda a contagem na variável "x"
x = conta_acima_media(v1)

# Exibe o resultado
print(f"{x} elementos estão acima da média")