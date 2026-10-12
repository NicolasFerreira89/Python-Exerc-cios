from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar ?')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total} -', end = '')
    print(f' Deu Par' if total % 2 == 0 else ' Deu ìmpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce ganhou!!')
            v += 1
        else:
            print('Voce perdeu!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce ganhou!!')
            v += 1
        else:
            print('Voce perdeu!!')
            break
    print('Vamos jogar novamente...')

print(f'Game Over!! Você venceu {v} vezes')
