import os
os.system("cls")

'''
# Síntaxe do for:

for <var_contadora> in range(<inicio>, <fim> - 1, <incremento>) # range verifica intervalos
    <bloco de repeticao>
'''

# print exibe a mensagem na tela e pula uma linha

# Exibir "Bom dia" na tela 10x
for volta in range (1, 10, 1):
    print("Bom dia", end = " | ")

print()

# while
volta = 1
while volta < 11:
    print("Bom dia", end = " | ")
    volta = volta + 1

print()

# while True
volta = 1
while True:
    print("Bom dia", end = " | ")
    volta = volta + 1
    if volta >= 11:
        break # break -> força a saída do laço