"""
8. Um caixa eletrônico dispensa cédulas de 10, 20, 50 e 100 reais. Dada uma 
quantia pelo usuário, informar quantas cédulas de cada valor são necessárias 
para compor este montante.
Entrada: 380
Saída: 
3 cédulas de 100 
1 cédula de 50 
1 cédula de 20 
1 cédula de 10
"""

cedula_1 = 100
cedula_2 = 50
cedula_3 = 20
cedula_4 = 10

quantia = int(input("Digite a quantia em reais: "))

qtd_100 = quantia // cedula_1
# 3 = 380 // 100 ( 3 cédulas de 100)
quantia = quantia % cedula_1
# 80 = 380 % 100 (Sobrou 80 reais)

qtd_50 = quantia // cedula_2
# 1 = 80 // 50 (1 cédula de 50)
quantia = quantia % cedula_2
# 30 = 80 % 50 (Sobrou 30 reais)

qtd_20 = quantia // cedula_3
# 
quantia = quantia % cedula_3

qtd_10 = quantia // cedula_4
quantia = quantia % cedula_4

# - Exibir o resultado 
print(qtd_100, "cédulas de ", cedula_1)
print(qtd_50, "cédulas de ", cedula_2)
print(qtd_20, "cédulas de ", cedula_3)
print(qtd_10, "cédulas de ", cedula_4)