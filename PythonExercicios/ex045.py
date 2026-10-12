from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print(''''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura\n''')
jogador =int(input('Qual sua jogada? '))
print('JÓ...')
sleep(1)
print('KEN...')
sleep(1)
print('Pô!!!')
sleep(1)
print('-=-'*11)

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-'*11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')

