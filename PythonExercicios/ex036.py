casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Salario do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
minimo = salario * 30 / 100

prestacao = casa / (anos * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f} '.format(casa, anos, prestacao))

if prestacao <= minimo:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')
