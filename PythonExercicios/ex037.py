num = int(input('Digite um nunmero inteiro: '))
print('''Escolha uma das bases para conversão 
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int (input('Sua opção: '))

if opção ==1:
    print('{} Converção para BINÁRIO {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Converção para OCATAL {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Converção para HEXADECIMAL {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')