
num1 = float(input('Digite um número: \n'))
num2 = float(input('Digite um número: \n'))
num3 = float(input('Digite um número: \n'))

print('Os números em ordem decrescente são: ')
if num1 > (num2 and num3):
    if num2 > num3:
        print(num1, num2, num3)
    if num3 > num2:
        print(num1, num3, num2)
elif num2 > (num1 and num3):
    if num1 > num3:
        print(num2, num1, num3)
    if num3 > num1:
        print(num2, num3, num1)
elif num3 > (num1 and num2):
    if num1 > num2:
        print(num3, num1, num2)
    if num2 > num1:
        print(num3, num2, num1)
