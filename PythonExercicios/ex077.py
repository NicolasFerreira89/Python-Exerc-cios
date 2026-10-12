palavras = ('aprender', 'programar', 'linguagem', 'python' 'curso', 'gratis', 'estudar', 'prativar', 'trabalhar', 'mercado', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos - ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end='')
