n = s = q = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    q += 1
    s += n
print(f'A soma vale {s} e foram digitados {q} números')
