velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Multado!! Você excedeu o limite permitido de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve paga uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança!')