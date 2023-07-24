
a = int(input('Digite um valor A:'))
b = int(input('Digite um valor B:'))
c = int(input('Digite um valor C:'))

if a + b <= c or a + c <= b or b + c <= a:
    print('Estes três lados não formam um triângulo.')
elif a == b == c:
    print('Este é um triângulo equilátero.')
elif a == b or c == a or a == c:
    print('Este é um triângulo isósceles.')
else:
    print('Este é um triângulo escaleno.')
