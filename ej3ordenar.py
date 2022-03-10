def maximoMinimo(lista):
    lista_ordenada=[]
    lista_reversa=[]
    for i in sorted(lista):
        lista_ordenada.append(i)
        min=lista_ordenada[0]
    for i in reversed(lista_ordenada):
        #como ya tengo la lista ordenada de menor a mayor le doy la vuelta y cojo el 1 elemento 
        lista_reversa.append(i)
        max=lista_reversa[0]
    return min,max