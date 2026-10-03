import os
os.system("cls")

pedido = input("Qual o seu pedido tipo de pedido? (Troca, devolução ou suporte) ").strip().lower()
prioridade = int(input("Qual o número de prioridade? (1, 2 ou 3) "))

match (pedido, prioridade):
    case ("troca" | "devolução", 1):
        print("Setor pós-venda. Atendimento imediato")

    case ("troca" | "devolução", 2):
        print("Setor pós-venda. Atendimento de até 4 horas")

    case ("troca" | "devolução", 3):
        print("Setor pós-venda. Atendimento até 1 dia útil")

    case ("suporte", 1):
        print("Setor técnico. Atendimento imediato")

    case ("suporte", 2):
        print("Setor técnico. Atendimento de até 4 horas")

    case ("suporte", 3):
        print("Setor técnico. Atendimento de até 1 dia útil")

    case _:
        print("Pedido ou valor inválido")