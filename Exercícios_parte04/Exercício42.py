
base = float(input('Digite o salário base do funcionário:'))

print(f'O salário final do funcionário será de {(base * 1.05) - (base * 0.07)}')

preco = float(input('Digite o preço da compra:'))

avista = (preco * 0.9)
parcel = (preco / 3)
comavista = (avista * 0.05)
comparcel = (parcel * 0.05 * 3)

print(avista, parcel, comavista, comparcel)
