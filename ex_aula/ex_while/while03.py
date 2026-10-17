import os 
os.system("cls")

# Exemplo: Calcular a média de duas notas do usuário, enquanto for digitado S no continuar
# v2.0 - Obrigar o usuário a digitar "S" ou "N" maiúsculo ou minúsculo em opção

opcao = "s"

while True: 
    nota1 = float(input("Nota 1: "))
    if nota1 < 0 or nota1 > 10:
        print("Nota inválida!")
        continue # Interrompe o laço e volta para o começo do laço

    nota2 = float(input("Nota 2: "))
    if nota1 < 0 or nota1 > 10:
        print("Nota inválida!")
        continue

    media = (nota1 + nota2) / 2

    print(f"A média das notas {nota1} e {nota2} é {media}")

    opcao = input("Deseja continuar? [S]im ou [N]ão: ")

    while opcao != "s" and opcao != "S" and opcao != "n" and opcao != "N":
        opcao = input("ERRO!! Digite S ou N: ")

    else:
        if opcao == "n" or opcao == "N":
            break # Interrompe a execução do laço

# Ou
    # opcao = input("Deseja continuar? [S]im ou [N]ão: ")
    # opcao.upper()

    # while opcao != "S" and opcao != "N":
    #     opcao = input("ERRO!! Digite S ou N: ")

    # else:
    #     if opcao == "n" or opcao == "N":
    #         break # Interrompe a execução do laço

# Ou
    # opcao = input("Deseja continuar? [S]im ou [N]ão: ")

    # while opcao.upper() not in ["S", "N"]:
    #     opcao = input("ERRO!! Digite S ou N: ")

    # else:
    #     if opcao == "n" or opcao == "N":
    #         break # Interrompe a execução do laço