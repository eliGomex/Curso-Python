"""
user_name = input('Digite seu nome: ')
age_name = input('Digite sua idade: ')

if (user_name == '') or (age_name == ''):
    print('Desculpe, você deixou campos vazios')
    print(type(user_name))
    print(type(age_name))
else:
    print(f'Seu nome é {user_name}')
    print(f'Seu nome invertido é {user_name[::-1]}')
    print(f'A primeira letra do seu nome é {user_name[0]}')
    print(f'A primeira letra do seu nome é {user_name[4]}')
    print(type(user_name))
    print(type(age_name))
"""

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")

