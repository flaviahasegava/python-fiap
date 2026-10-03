import os
os.system("cls")

cor = input("Informe a ação do motorista: ").strip().lower()

match cor:
    case "vermelho":
        print("Parar")

    case "amarelo":
        print("Atenção")

    case "verde":
        print("Seguir")

    case _: 
        print("Cor inválida. Essa opção não existe")