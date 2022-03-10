ordenada = []
def ordenarTabla(tabla):
    
    minimo = min(tabla)
    if len(tabla) == 1:
        ordenada.append(tabla[0])
        return ordenada
    else:
        ordenada.append(minimo)
        tabla.remove(minimo)
            
    return  ordenarTabla(tabla)

def ordenarTabla(tabla):
    ordenada = ordenarTabla(tabla)
    return ordenada
