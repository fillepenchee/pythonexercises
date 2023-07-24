
distancia = float(input('Quantidade de kms percorridos? \n'))
gasolina = float(input('Quantidade de litros de gasolina consumidos? \n'))

consumo = (distancia / gasolina)

print(f'Este carro está fazendo {consumo} km/l.')

if consumo < 8:
    print('Venda o carro!')

if 8 < consumo < 14:
    print('Econômico!')

if consumo > 12:
    print('Super econômico!')
