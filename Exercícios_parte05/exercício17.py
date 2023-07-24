
h = float(input('Digite a altura do trapézio: \n'))
bmaior = float(input('Digite o tamanho da base maior do trapézio: \n'))
bmenor = float(input('Digite o tamanho da base menor do trapézio: \n'))

if h and bmaior and bmenor > 0:
    print(((bmaior + bmenor) * h) / 2)
else:
    print('Pelo menos um dos valores informados é inválido.')
