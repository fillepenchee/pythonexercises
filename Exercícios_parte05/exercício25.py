
a = float(input('Digite o valor de a: \n'))
b = float(input('Digite o valor de b: \n'))
c = float(input('Digite o valor de c: \n'))

if a == 0:
    print('Não é uma equação de 2o grau.')

delta = (b ** 2) - (4 * a * c)

x = (-b + (delta ** (1 / 2))) / 2 * a
x2 = (-b - (delta ** (1 / 2))) / 2 * a

raiz = ((a * x) ** 2) + (b * x) + c
raiz2 = ((a * x2) ** 2) + (b * x2) + c

if delta < 0:
    print('Não existe raiz real.')

if delta == 0:
    print(f'Existe uma raiz real: {raiz}')

if delta > 0:
    print(f'Existem duas raízes reais: {raiz} e {raiz2}')
