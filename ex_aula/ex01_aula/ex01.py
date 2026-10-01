import os
os.system("cls")

# - Digitar um número inteiro
numero = int(input("Digite um número: "))
# - Calcular o antecessor
antecessor = numero - 1 
# - Calcular o sucessor
sucessor = numero + 1
# - Exibir o resultado
print(f"""
    Número: {numero}
    Antecessor: {antecessor}
    Sucessor: {sucessor}
""")