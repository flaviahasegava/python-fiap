import os 
os.system("cls")

# Exemplo: Calcular o dobro de um número e verificar se o usuário quer continuar ou não

opcao = "s"
qtd = 0

while opcao == "s" or opcao == "S":
    num = float(input("Número: ")) 
    dobro = num * 2

    print(f"O dobro de {num} é {dobro}")
    qtd = qtd + 1 # ou qtd += 1 

    opcao = input("Continuar? [S]im ou [N]ão: ")

else: # É executado ao terminar o laço se não há interrupção / Não sai do laço
    print("Programa terminado!")


print(f"O programa foi executado {qtd} vezes")