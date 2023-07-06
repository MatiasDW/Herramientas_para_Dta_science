def comprobar_parentecis(texto):
    pila = list()
    for letra in texto:
        
        
        
        
assert(comprobar_parentecis("([{}])"))
assert(not comprobar_parentecis("{(})"))
assert(not comprobar_parentecis("([{(}])"))
assert(comprobar_parentecis("(([{}]))"))
assert(comprobar_parentecis("{}([{}])"))
assert(not comprobar_parentecis("){}(p{}])"))
