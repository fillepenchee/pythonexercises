
num1 = int(input('Digite um número: \n'))
harmonic = 1
n = 1

while n in range(1, (num1 + 1)):
    harmonic = harmonic + (1 / n)
    n = n + 1

print(f'O número harmônico de {num1} é {harmonic}.')
