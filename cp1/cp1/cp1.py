import os
os.system("cls")

salario = float(input('Qual o seu salário? R$ '))
qtd_faltas = int(input('Qual a quantidade de faltas? '))

if salario < 0 and qtd_faltas < 0:
    print('ERRO! Digite um salário positivo')
    
else:
    salario_minimo = 1302
    if salario <=  2 * salario_minimo:
        reajuste = 0.0645

    elif salario <= 5 * salario_minimo:
        porcentagem_reajuste = 0.455

    else:
        porcentagem_reajuste = 0.0289

    salario_reajustado = salario + (salario * porcentagem_reajuste)

    if qtd_faltas == 0:
        bonus = 1302
        salario_reajustado += salario_minimo
        print('Você receberá um bônus de salário mínimo!')

    elif faltas == 1:
        bonus = 500
        salario_reajustado += 500
        print('Seu bônus foi de 500 reais')

    else:
        bonus = 0
        salario_reajustado += 0
        print('Você não receberá o bônus')

    salario_total = salario_reajustado
    
    print(f"""
    Salário: R$ {salario:.2f}
    Quantidade de faltas: {qtd_faltas}

    Relatório: 
    --------------------------------------------------
    Salário.................: R$ {salario:.2f}
    Salário Reajustado......: R$ {salario_reajustado:.2f}
    Bônus...................: R$ {bonus:.2f}
    Ganho total.............: R$ {salario_total:.2f}
    """)