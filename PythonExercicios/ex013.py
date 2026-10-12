sal = float(input('Qual o salario do funcionário ? R$'))
novo = sal + (sal*15/100)

print('O novo salário será de R$ {:.2f} com 15% de aumento'.format(novo))