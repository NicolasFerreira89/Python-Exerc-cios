m = float(input('Digite a distancia em metros: '))
cm = m * 100
mm = m * 1000
km = m / 1000

print('A distancia em metros é {:.0f}, em centímetros é {:.0f}, em milimetros é {:.0f}, e em Kilometros é {:.1f}'.format(m, cm, mm, km))