import os
os.system("cls")

# Caixa eletrônico simplificado

saldo = 500

while True:
    print(f"""
    CAIXA ELETRÔNICO
    ========================
    1 - Saldo
    2 - Depositar
    3 - Sacar
    4 - Sair
    ========================
    """)

    opcao = input("Escolha uma opção: ").strip().lower()
    
    match opcao:
        case "1" | "saldo":
            print(f"\nSaldo atual: R$ {saldo:.2f}")

        case "2" | "depositar":
            depositar = float(input("\nDepositar: R$ "))
            if depositar > 0:
                saldo += depositar
                print("Depósito realizado!")

            else:
                print("\nErro! Valor negativo. O valor deve ser maior que zero.")

        case "3" | "sacar":
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            sacar = float(input("Sacar: R$ "))

            if sacar <= 0:
                print("Erro! Valor negativo. O valor do saque deve ser maior que zero.")
            
            elif sacar > saldo:
                print("\nATENÇÃO: Saque negado.\nO valor a sacar é maior que o saldo.\nEscolha outra opção!")

            else:
                saldo -= sacar
                print("Saque realizado!")

        case "4" | "sair":
            print("\nSaindo...")
            break

        case _:
            print("\nOpção inválida!\nEscolha novamente uma opção!")

print(f"Saldo atual: R$ {saldo:.2f}")