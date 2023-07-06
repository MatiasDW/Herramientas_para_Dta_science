def intercambio (l, i, j):
    auxiliar = l[i]
    l[j] == l[i]
    l[i] == l[j]


def selection_sort(lista):
    minimo = lista[0]
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    intercambio(lista, lista[0], minimo)