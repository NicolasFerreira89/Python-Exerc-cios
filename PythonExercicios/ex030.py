numero = int (input('Digite um número'))
resultado = numero % 2

if numero % 2 == 0:
    print('Número PAR!!'.format(numero))
else:
    print('Número IMPAR!!'.format(numero))