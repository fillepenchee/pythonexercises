
altura = float(input('Digite a altura da pessoa em m: \n'))
peso = float(input('Digite o peso da pessoa (em kg): \n'))

if altura < 1.20:
    if peso < 60.0:
        print('Categoria A')
    elif 60.0 <= peso <= 90.0:
        print('Categoria D')
    elif peso > 90:
        print('Categoria G')
if 1.20 <= altura <= 1.70:
    if peso < 60.0:
        print('Categoria B')
    elif 60.0 <= peso <= 90.0:
        print('Categoria E')
    elif peso > 90:
        print('Categoria H')
if altura > 1.70:
    if peso < 60.0:
        print('Categoria C')
    elif 60.0 <= peso <= 90.0:
        print('Categoria F')
    elif peso > 90:
        print('Categoria I')
