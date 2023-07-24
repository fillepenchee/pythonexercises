
num1 = float(input('Digite um número:'))
div3 = num1 % 3
div5 = num1 % 5

if div3 == 0:
    print(f'{num1} é divisível por três.')
else:
    print(f'{num1} não é divisível por três.')

if div5 == 0:
    print(f'{num1} é divisível por cinco.')
else:
    print(f'{num1} não é divisível por cinco.')

if (div3 == 0) and (div5 == 0):
    print(f'{num1} não serve, pois é divisível tanto por 3 quanto por 5.')
else:
    print(f'{num1} serve, pois ou é não divisível por 3, ou é não divisível por 5.')
