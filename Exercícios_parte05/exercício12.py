
import math as math

numero = float(input('Digite um número:'))

if numero <= 0:
    print('Número inválido.')
else:
    print(math.log(numero))
    # ou então print(f"{math.log(numero)}")