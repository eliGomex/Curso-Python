print('-----CALCULADORA DE IMC-----')


nome = input('Digite seu nome: ')
altura_metros = float(input('Digite seua altura em metros: '))
peso = float(input('Digite seu peso em quilogramas: '))
imc = peso / (altura_metros*altura_metros)
#F-strings
print(f'{nome} seu peso é {peso}, sua altura é {altura_metros} e seu IMC é {imc:.2f}')
