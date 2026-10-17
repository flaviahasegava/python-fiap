# Solicite ao usuário dois números inteiros, representando o início e o fim de um intervalo.

# O programa deverá exibir todos os números compreendidos entre os valores informados, incluindo o valor inicial e o valor final, obedecendo às seguintes regras:

# Se o valor inicial for menor que o valor final, exiba os números em ordem crescente.

# Se o valor inicial for maior que o valor final, exiba os números em ordem decrescente.

# Se os dois valores forem iguais, exiba somente o número informado.


# Solicita o inicio e o fim
inicio = int(input("Digite o início: "))
fim = int(input("Digite o final: "))

print("[", end = "")

# Verifica se o início é menor que o fim (Ordem crescente)
if inicio < fim:
    for volta in range(inicio, fim + 1, 1):

        # Verifica se o número de voltas é igual ao final para fechar com colchetes sem colocar vírgula no final
        if volta == fim:
            print(volta, end = "")

        else:
            print(volta, end = ", ")

# Verifica se o início é maior que o fim (Ordem decrescente)
elif inicio > fim:
    for volta in range(inicio, fim - 1, -1):

        if volta == fim:
            print(volta, end = "")

        else:
            print(volta, end = ", ")

else:
    print(inicio, end = "")

print("]")