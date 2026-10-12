larg = float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))

area = larg * alt

print('Sua parede tem a dimensão de {:.1f} x {:.1f} metros e sua área é de: {}m² '.format(larg, alt, area))

tinta = area / 2
print('Para pintar essa parede, é necessário de {}L de tinta'.format(tinta))