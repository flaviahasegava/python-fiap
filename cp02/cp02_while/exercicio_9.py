import os
os.system("cls")

# Controle de estacionamento

total_veiculos = 0
total_arrecadado = 0

while True:
    placa = input("Placa: ").strip().upper()

    if placa == "FIM":
        break

    horas = int(input("Horas: "))

    if horas < 0:
        print("Horas inválidas! Digite um valor maior que zero.")
        break

    valor = 8 + (horas - 1) * 5

    if horas > 8:
        valor += 20

    print(f"{placa}: R$ {valor:.2f}")

    total_veiculos += 1
    total_arrecadado += valor

print(f"""
Veículos atendidos: {total_veiculos}
Total arrecadado: R$ {total_arrecadado:.2f}
""")