#versão 1
minha_lista = []
n = 0
while n < 6:
    minha_lista.append(int(input("Digite um número: \n")))
    n += 1
print(minha_lista)
minha_lista.reverse()
print(minha_lista)

#versão 2
minha_lista2 = []
n = 0
while n < 6:
    minha_lista2.append(int(input("Digite um número: \n")))
    n += 1
print(minha_lista2)
minha_lista2_invertida = minha_lista2[::-1]
print(minha_lista2_invertida)