
custo = int(input('Insira o custo de fábrica do veículo: \n'))

if custo <= 12000:
    custo = custo + (custo * 0.05)
elif 12000 < custo <= 25000:
    custo = custo + (custo * 0.25)
else:
    custo = custo + (custo * 0.35)

print(f'O custo final para o consumidor é de {custo}.')
