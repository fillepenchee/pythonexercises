
valor = 0
counter = 0
counter2 = 0

while counter in range(0, 10):
    valoruser = int(input('Digite um valor inteiro: \n'))
    counter = counter + 1
    if valoruser >= 0:
        valor = valoruser + valor
        counter2 = counter2 + 1

valor = (valor / counter2)

print(f'A média dos números digitados é {valor}.')
