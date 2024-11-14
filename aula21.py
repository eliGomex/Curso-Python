#Operadores Logicos
# and (e) or (ou) not (não)
# and todas as condições precisam ser verdadeiras
#se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy 0 0.0 '' False
# Tambem existe o tipo none que é usado para representar um não valor
# Avaliação de curto circuito
"""
------- AND ---------------
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '150123'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Logado')
else:
    print('Acesso não permitido')
"""
"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '150123'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Logado')
else:
    print('Acesso não permitido')
"""