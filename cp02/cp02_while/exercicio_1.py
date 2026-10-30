import os
os.system("cls")

# Acesso com três tentativas

tentativas = 1

senha_usuario = input("Senha: ")

while senha_usuario != "1234":
    senha_usuario = input("Acesso negado. Digite novamente!\nSenha: ")
    tentativas += 1

    if tentativas >= 3:
        print("Acesso negado.\nNúmero de tentativas ultrapassadas!")
        break

    continue

else:
    print("Acesso PERMITIDO.")

print(f"Número de tentativas: {tentativas}")