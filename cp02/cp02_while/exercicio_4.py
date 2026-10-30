import os
os.system("cls")

# Jogo de adivinhação
# Número secreto = 18

palpite = 0
tentativas = 0

while palpite != 18:
    palpite = int(input("Palpites: "))

    if palpite < 0 or palpite > 100:
        print("ERRO! Apenas números de 0 a 100.\n")
        continue
    
    tentativas += 1

    if palpite > 18:
        print(f"\nSeu palpite: {palpite}\nTente um número menor.\n")

    elif palpite < 18:
        print(f"\nSeu palpite: {palpite}\nTente um número maior.\n")
    
    if tentativas >= 7 and palpite != 18:
        print("Você usou as 7 tentativas.\nSuas tentativas de palpites acabaram.")
        break

if palpite == 18:
    print(f"Seu palpite: {palpite}\nParabéns! Você acertou em {tentativas} tentativas!")