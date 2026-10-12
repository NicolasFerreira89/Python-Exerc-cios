real = float(input('Quantos Reais você tem ? '))
dolar = real / 5.18
euro = real / 5.97
yuan = real / 0.77

print('Com R${:.2f} você pode comprar: \n US${:.2f}\n EUR {:.2f} \n CNY {:.2f}'.format(real, dolar, euro, yuan))