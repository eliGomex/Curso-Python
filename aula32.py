"""
num_Int = int(input('Digite um número inteiro: '))

verifica_Paridade = num_Int % 2

if verifica_Paridade == 0:
    print('Esse número é PAR')
else:
    print('Esse número é IMPAR')

informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'
#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')
"""
try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'
    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
"""

"""
nome_Usuário = input('Qual seu nome: ')
hora_Atual = int(input('Que horas são: '))

if hora_Atual <= 11:
    print(f'Bom dia {nome_Usuário}')
elif (hora_Atual > 11) and (hora_Atual <= 17):
    print(f'Boa Tarde {nome_Usuário}')
elif  (hora_Atual > 17) and (hora_Atual <= 23):
    print(f'Boa Noite {nome_Usuário}')

"""
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')
"""
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""
"""
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')

"""

nome_Usuário = input('Qual seu nome: ')
nome = len(nome_Usuário)

if nome <= 4:
    print('Seu nome é curto')
elif (nome > 4) and (nome <= 6):
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
