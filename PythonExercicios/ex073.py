times = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Cruzeiro', 'Bahia', 'Bragantino', 'Atlético-MG', 'Corinthians',
        'Coritiba', 'Botafogo', 'Vitória', 'São Paulo', 'Internacional', 'Santos', 'Grêmio', 'Mirassol', 'Remo', 'Vasco', 'Chapecoense')
print('-='*20)
for t in times:
    print(t)
print('-='*20)

print(f'Os 5 primeiros são: {times[0:6]}')
print('-='*20)
print(f'Os 4 ultimos são: {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*20)
print(f'O São Paulo está na: {times.index("São Paulo")+1}ª posição')