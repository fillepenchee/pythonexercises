
x = int(input('Digite um número inteiro positivo: \n'))
y = int(input('Digite mais um número inteiro positivo: \n'))
z = int(input('Digite mais um número inteiro positivo: \n'))

media = int(input('Escolha o tipo de média desejada: \n 1-Geométrica'
                  '\n 2-Ponderada \n 3-Harmônica \n 4-Aritmética: \n'))

if media == 1:
    print(f'A média geométrica é {(x * y * z) ** (1/3)}')

if media == 2:
    print(f'A média ponderada é {(x + (2 * y) + (3 * z)) / 6}')

if media == 3:
    print(f'A média harmônica é {1 / ((1/x) + (1/y) + (1/z))}')

if media == 4:
    print(f'A média aritmética é {(x + y + z) / 3}')
