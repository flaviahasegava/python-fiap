import os
os.system("cls")

# Pré-condicional (while) - Não sabe a quantidade de voltas (Perguntar e executar)
# Pós-condicional (while True) - Obrigado a dar apenas uma volta (Executar e perguntar)
# Contadora (for) - Sabe a quantidade de voltas

# Laço condicional while - usado para quantidade imprevistas de voltas
# Exemplo: somar números até que seja digitado zero
# ENTRADA: 4 5 1 7 3 4 1 0     SAÍDA: 15

# Acumuladores (Variável acumuladora usa ela mesma na conta / Sempre inicializar com um valor)
soma = 0
n = 1

while n != 0:
# -----------------------------------------------
# Ler os números (S)- Redundante / Repetitivo
    n = float(input("Número: "))
    
# Somar os números (S)
    soma = soma + n
# -----------------------------------------------
# Exibir a somatória (N)
print(f"Somatória: {soma}")