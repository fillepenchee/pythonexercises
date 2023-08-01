
valor = 0
counter = 0

while counter in range(0, 10):
    valor = valor + int(input('Digite um valor inteiro: \n'))
    counter = counter + 1

valor = (valor / 10)

print(f'A média dos números digitados é {valor}.')
