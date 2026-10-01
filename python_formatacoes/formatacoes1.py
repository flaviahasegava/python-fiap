import os 
os.system("cls")

# ========= FORMATAÇÕES DE SAÍDA DE DADOS
# Clássica vírgula: separa quaisquer tipos de dados (\n caractere de scape)
nome = "Edson"
idade = 32 
altura = 1.71

print("Nome:", nome, "Idade: ", idade, "Altura:", altura)
print("Nome:", nome, "\nIdade: ", idade, "\nAltura:", altura)
# Pesquisar outros caracteres \

# Usando o + (Apenas strings, o + junta strings, mas não da espaço)
os.system("cls")
nome = "Edson"
sobrenome = "de Oliveira"
print("Nome:" + nome + " " + sobrenome)
print("Nome: " + nome + " Idade: " + str(idade) + " Altura: " + str(altura))

# Casting - Mudança de tipo do dado (int, str, float, bool)

# Função format() - Fica em apenas um par de aspas (nome = 0, idade = 1 e altura = 2 / Modificar os números muda a ordem)
# print("Nome: {1}\nIdade: {0}\nAltura: ".format(nome, idade, altura))
os.system("cls")
print("Nome: Idade: Altura: ".format(nome, idade, altura))
print("Nome: {1}\nIdade: {0}\nAltura: {2}\n".format(nome, idade, altura))
print("Nome: {n}\nIdade: {i}\nAltura: {a}\n".format(n = nome, i = idade, a = altura))
# n, i e a apelidos momentâneos

# Formatação f print
os.system("cls")
print(f"Nome: {nome}\nIdade: {idade}\nAltura: {altura}\n")

os.system("cls")
# Formatação dados float
valor1 = 23.4546
valor2 = 2344.4
valor3 = 2323424.4545
# Pode ser tudo na mesma linha 
print(f"Valor 1: {valor1}")
print(f"Valor 2: {valor2}")
print(f"Valor 3: {valor3}")
# :.2f formata com duas casas decimais
print(f"\nValor 1: R$ {valor1:.2f}") 
print(f"Valor 2: R$ {valor2:.2f}")
print(f"Valor 3: R$ {valor3:.2f}")
# 10 espaços com 2 casas decimais
print(f"\nValor 1: R$ {valor1:10.2f}") 
print(f"Valor 2: R$ {valor2:10.2f}")
print(f"Valor 3: R$ {valor3:10.2f}")
print(valor1 * 2)

os.system("cls")
nome1 = "Edson de Oliveira"
nome2 = "Maria da Silva Nogueira Pereira"
idade1 = 9
idade2 = 35
# 5d dados decimais inteiros
# print(f"Nome: {nome} | Idade: {idade:05d}")
# 35 caracteres
print(f"Nome: {nome1:35} | Idade: {idade1:3d}")
print(f"Nome: {nome2:35} | Idade: {idade2:3d}")

# Triple Quotes ''' ou """
os.system("cls")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")

print(f"""
    Nome: {nome}
    Idade: {idade}
    Altura: {altura}
""")

# Formatação % - Herdada da linguagem C
