"""
Formatação básica strings
s - string
d e i - int
f - float
x e X - Hexadecimal

<número de digito>f

x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro

Sinal - + ou -
ex.: 0>-100,.1f
conversion flags - !r !s !a

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.1514541545465:0=+10,.1f}.')
print(f'O Hexadeximal de 1500 é{1500:08X}.')
print('f{variavel!r}')



