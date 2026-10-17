"""
PROBLEMA: 
Um caixa eletrônico dispensa cédulas de 10, 20, 50 e 100 reais. Dada uma 
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

# - Digitar a quantia em reais
quantia = float(input("Digite a quantia em reais: "))
# - Calcular quantas cédulas são necessárias para compor o montante
qtd_100 = quantia // cedula_1
quantia = quantia % cedula_1

qtd_50 = quantia // cedula_2
quantia = quantia % cedula_2

qtd_20 = quantia // cedula_3
quantia = quantia % cedula_3

qtd_10 = quantia // cedula_4
quantia = quantia % cedula_4

# - Exibir o resultado 
print(qtd_100, "cédulas de ", cedula_1)
print(qtd_50, "cédulas de ", cedula_2)
print(qtd_20, "cédulas de ", cedula_3)
print(qtd_10, "cédulas de ", cedula_4)

