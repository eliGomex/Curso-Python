# CONDICIONAIS

#if / elif / else
#se / se não se/ se não

#else e elif dependem do if
#So executa condições verdadeiras e else caso não haja uma verdadeira

condicao1 = False
condicao2 = True
condicao3 = False
condicao4 = False


if condicao1:
    print('Codigo para condição 1')
elif condicao2:
    print('Codigo para condição 2')
elif condicao3:
    print('Codigo para condição 3')
elif condicao4:
    print('Codigo para condição 4')
else:
    print('Nenhuma condição satisfeita')

if 10 == 10:
    print('Outro if')