import os
os.system("cls")

# VETOR

# Variável indexada é criada entre colchetes
#    0   1   2   3   4      <=== índices
v = [34, 55, 29, 12, 87] #  <=== dados  
# Variável é sempre o "v", mas o índice pode mudar

# Exibindo o conteúdo do vetor
print(v)

# Exibindo uma posição específica
# print(v[3]) <--- Mostra o valor do índice 3 do "v"
v[0] = int(input("Valor: ")) # Muda o valor do índice 0 para a entrada do usuário
print(v)

if v[0] > v[4]:
    print("A posição 0 é maior que a 4")

else:
    print("A posição 4 é maior que o 0")