import os
os.system("cls")

''' 
Considere o vetor v = [45, -89, 32, -12, 33]: 

3. Fazer um programa que peça um valor ao usuário e verifique se ele existe ou não no vetor. 
    >> Valor: 32 
    >> O valor 32 está no vetor 
'''

# Cria uma lista com 5 elementos
v = [45, -89, 32, -12, 33]

# Pede o valor ao usuário
numero = int(input("Valor: "))

# Laço de repetição
for i in range(0, 5, 1):

    # Verificar se o valor é igual ao elemento do vetor
    if numero == v[i]:
        # Mostra que existe o valor no vetor
        print(f"O valor {numero} está no vetor")

    else: 
        # Caso não tenha, mostra que não existe
        print("O valor não está no vetor")
        
        # Para o programa
        break