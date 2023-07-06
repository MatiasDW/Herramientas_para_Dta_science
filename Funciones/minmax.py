def min_fila(m, f):
    minimo = m[f][0]
    for j in range(len(m[0])):
        if m[f][j] < minimo:
            minimo = m[f][j]
    return minimo

def max_col(m, c):
    maximo = m[0][c]
    for i in range(len(m)):
        if (m[i][c] > maximo):
            maximo = m[i][c]
    return maximo

def min_max(m):
    
    minmax = list()
    n_filas = len(m)
    for i in range(n_filas):
       minimo = min_fila(m, i) 
       maximo = max_col(m, i)
       minmax.append([minimo, maximo])
    return minmax
       

#m[1][0] es el minimo de la fila m[i][l] es el maximo de la columna    
assert (min_max([[17, 4],
                 [1, 1]]) == [[4, 17],
                              [1, 4]])
    
assert (min_max([[1, 2, 3],
                 [3, 1, 2],
                 [2, 3, 1]]) == [[1, 3],
                                 [1, 3],
                                 [1, 3]])                              
                                 