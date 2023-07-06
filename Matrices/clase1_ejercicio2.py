'''Crea una funcion que devuelva el indice(posicion) del menor numero de la lista.
piedes asumir que no hay repeticiones y que la lista esta compuesta por numeros enteros'''


def indice_min_enteros(l):
    
     x = l[0] #incorporar algun valor de la lista para poder compararlo despues. en numpy es np.inf=numero infinito
     indice = 0
     for i in range(len(l)): #i en el largo de las lista l
         if l[i] < x:
             x = l[i]
             indice = i
     return indice


#l_numero_en_medio = [3, 4, 5, 20, 2, 7, 9]
l_numero_inicial = [0, 4, 5, 20, 2, 7, 9]
l_numero_final = [3, 4, 5, 20, 2, 7, 90]
l_negativos = [-3, -4, -5, -20, -2, -7, -9]

#assert(indice_min_enteros(l_numero_en_medio) == 4)
assert(indice_min_enteros(l_numero_inicial) == 0)
assert(indice_min_enteros(l_numero_final) == 4)
assert(indice_min_enteros(l_negativos) == 3)

