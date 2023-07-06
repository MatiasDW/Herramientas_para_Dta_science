'''Encontar Maximo en lista de N naturales, asumiendo la no repeticion de elementos,
sin  usar funcion min, max, etc.'''

def Max_naturales(l):
    x=0
    for i in range(len(l)): 
        if l[i] > x:
            x = l[i]
    return x


l_numero_en_medio = [3, 4, 5, 20, 2, 7, 9]
l_numero_inicial = [300, 4, 5, 20, 2, 7, 9]
l_numero_final = [3, 4, 5, 20, 2, 7, 90]

print(Max_naturales(l_numero_en_medio))

assert(Max_naturales(l_numero_en_medio) == 20)
assert(Max_naturales(l_numero_inicial) == 300)
assert(Max_naturales(l_numero_final) == 90)
