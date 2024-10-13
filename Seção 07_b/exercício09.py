#versão 1

minha_lista = []
n = 0
while n < 6:
    a = (int(input("Digite um número par: \n")))
    while a % 2 == 1:
        a = (int(input("O número não é par. Favor digitar um número par: \n")))
    minha_lista.append(a)
    n += 1
print(minha_lista)
minha_lista.reverse()
print(minha_lista)


#versão 2

minha_lista2 = []
n = 0
while n < 6:
    a = (int(input("Digite um número par: \n")))
    while a % 2 == 1:
        a = (int(input("O número não é par. Favor digitar um número par: \n")))
    minha_lista2.append(a)
    n += 1
print(minha_lista2)
minha_lista2_invertida = minha_lista2[::-1]
print(minha_lista2_invertida)
