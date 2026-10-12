from time import sleep

def cont(i, f ,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=-'*40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)


    if i < f:
        contador = i
        while contador <= f:
            print(f'{contador} ', end='')
            sleep(0.5)
            contador += p
        print('FIM')
    else:
        contador = i
        while contador >= f:
            print(f'{contador} ', end='')
            sleep(0.5)
            contador -= p
        print('FIM')

cont(1, 10, 1)
cont(10, 0, 2)
print('-=-'*40)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cont(i, f, p)