#Crea una funcion en donde se identifique si es una matriz diagonal o no y devuelava los valores en boolean, 
#asume que es una matriz cuadrada

def diagonal(m_diagonal):
    n_filas = len(m_diagonal)
    n_columnas = len(m_diagonal[0])
    for fila in range(n_filas):
        for columna in range(n_columnas):
            if fila != columna and m_diagonal[fila][columna] != 0: 
                    return False
    return True


m_diagonal = [[1, 0, 0],
              [0, 7, 3],
              [0, 0, 3]]
assert(diagonal(m_diagonal) == True)

m_no_diagonal = [[1, 0, 2],
                 [0, 7, 0],
                 [0, 0, 3]]
assert(diagonal(m_no_diagonal) == False)
