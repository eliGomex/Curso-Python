"""
Interpolação básica de strings

s - string
d e i - int
f - float
x e X - Hexadecimal

"""

nome = 'Elian'
preco = 10.15210
variavel = '%s o preço é R$%.2f' % (nome, preco) 
print(variavel)
print('Hexadecial de %d é %08X' % (1500, 1500))