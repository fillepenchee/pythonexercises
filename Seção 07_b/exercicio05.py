lista_a = [1,2,3,4,5,6,7,8,20,253]
lista_b = [205, 66, 883, 2392, 60, 337, 867890, 20, 253]

def conta_pares(qual_lista):
    n = 0
    lista_final = []
    while n < len(qual_lista):
        if qual_lista[n] % 2 == 0:
            lista_final.append(qual_lista[n])
        n += 1
    print(f"A lista {qual_lista} tem {len(lista_final)} números pares. São os seguintes: {lista_final}.")

conta_pares(lista_a)
conta_pares(lista_b)
