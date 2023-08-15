
mult3 = 0
mult5 = 0
mult3e5 = 0

for n in range(0, 1000):
    if n % 3 == 0:
        mult3 = mult3 + n

for p in range(0, 1000):
    if p % 5 == 0:
        mult5 = mult5 + p

mult3e5 = mult3 + mult5

for x in range(0, 1000):
    if x % 3 == 0 and x % 5 == 0:
        mult3e5 = mult3e5 - x

print(f'A soma dos divisores inteiros de 1000, excluindo o próprio, é {mult3e5}.')
