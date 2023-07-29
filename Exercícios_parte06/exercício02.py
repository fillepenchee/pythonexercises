
for x in range(1, 101):
    print(x)

y = 1

while y in range(1, 100):
    y = y + 1
    print(y)

# fiz um "do while" simulado em Python:

z = 1

while True:
    print(z)
    z = z + 1
    if z >= 101:
        break
