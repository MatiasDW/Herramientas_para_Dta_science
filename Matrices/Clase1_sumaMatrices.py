#Suma elementos de una matriz
"""Crea una funcion que devuelva la suma de todos los elementos de la matriz"""

'''
def suma_elementos(m):
    n_fila = len(m)  #Cuantas filas hay
    n_columnas = len(m[0]) #Cuantas columnas hay
    suma = 0
    for fila in range(n_fila):
        for columna in range(n_columnas):
            suma = suma + m[fila][columna]
    return(suma)
    


m = [[1, 2, 3],
     [2, 2, 2],
     [1, 2, 3]]

m2 = [[1, 2, 3],
      [2, 2, 2],
      [1, 2, 3],
      [1, 2, 3]]
assert(suma_elementos(m) == 18)
assert(suma_elementos(m2) == 24)'''


#Crea una funcion en donde se identifique si es una matriz diagonal o no y devuelava los valores en boolean, 
#asume que es una matriz cuadrada

def diagonal(m_diagonal):
    n_filas = len(m_diagonal)
    n_columnas = len(m_diagonal[0])
    es_diagonal = False
    for fila in range(n_filas):
        for columna in range(n_columnas):
            if fila == columna: 
                if m_diagonal[fila][columna] != 0:
                    es_diagonal = True
                else:
                    es_diagonal = False
            #####    
            else:
                if m_diagonal[fila][columna] == 0: 
                    es_diagonal = True
                else: 
                    es_diagonal = False
    return(es_diagonal)


m_diagonal = [[1, 0, 0],
              [0, 7, 3],
              [0, 0, 3]]
assert(diagonal(m_diagonal) == True)

m_no_diagonal = [[1, 0, 2],
                 [0, 7, 0],
                 [0, 0, 3]]
assert(diagonal(m_no_diagonal) == False)

