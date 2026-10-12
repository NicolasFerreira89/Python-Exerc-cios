def ficha(jog= '<desconhecido>', gol=0):
    print(f'O jogadro {jog} fez {gol} gols no campeonato.')


n = str(input('Informe o nome do jogador: '))
g = str(input('Número de gols'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)