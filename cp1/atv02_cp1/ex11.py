import os
os.system("cls")

'''
11. Verificação com not 
Pergunte ao usuário se o sistema está bloqueado, usando S ou N. Utilize o operador not em uma condição 
lógica para informar se o usuário pode continuar. Considere que somente "S" representa sistema bloqueado.
'''

# Solicitar a resposta se o sistema está bloqueado
status_sistema = str(input("O sistema está bloqueado? (S/N) "))
# Verificar se é possível continuar 
if not status_sistema == "S":
    print("Pode continuar.")
else:
    print("O sistema está bloqueado.")