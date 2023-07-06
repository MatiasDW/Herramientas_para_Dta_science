def habitantes(m, ciudad):
    filtro = [] 
    for i in range(len(m)):
        if m[i][1] == ciudad:
            filtro.append(m[i])
    return filtro

def ricos(m, ciudad):
    rico = []
    presu = 0
    for i in range(len(m)):
        if m[i][2] >presu and m[i][1] == ciudad:
            presu = m[i][2]
            rico = m[i]
    return rico 
    
    
    
personas = [['Dombina','Buenos Aires',37676]
            ['Heredia','Buenos Aires',42251]
            ['Dictina','Buenos Aires',58760]
            ['Simplicia','Buenos Aires',39378]
            ['Cleta','Buenos Aires',53306]
            ['Nicomeda','Sucre',50374]
            ['Edelvina','Sucre',37583]
            ['Cita','Sucre',52048]
            ['Nicomeda','Sucre',50374]
            ['Floria','Sucre',35484]
            ['Carriona','Sucre',40362]
            ['Armelinda','Bogota',47029]
            ['Fernandina','Bogota',47873]
            ['Piedrasantas','Bogota',52538]
            ['Ermilia','Quito',57647]
            ['Aracelia','Quito',55043]
            ['Wenche','Quito',43762]
            ['Oristilia','Lima',43762]]

assert(habitantes(personas, 'Sucre') == [['Nicomeda', 'Sucre', 50374],
                                         ['Edelvina','Sucre',37583],
                                         ['Cita','Sucre',52048],
                                         ['Floria','Sucre',35484],
                                         ['Carriona','Sucre',40362]])
assert(habitantes(personas, 'Lima') == [['Oristilia','Lima',43762]])
assert(ricos(personas, 'Buenos Aires') ==[['Dictina','Buenos Aires',58760],
                                          ['Cleta','Buenos Aires',53306]])
assert(ricos(personas, 'Lima') == [['Oristilia','Lima',43762]])
                                         