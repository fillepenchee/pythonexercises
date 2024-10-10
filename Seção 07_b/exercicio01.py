a = []
a.append(1)
a.append(0)
a.append(5)
a.append(-2)
a.append(-5)
a.append(7)

print(a)

soma = a[0] + a[1] + a[5]

print(soma)

a.insert(4, 100)
print(a)

for num in a:
    print(f'{num}')