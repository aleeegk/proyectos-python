def snail_length(x, y):
    if x == 0 and y == 0:
        return 0
        
    # Determinar en qué capa 'k' se encuentra el punto
    k = max(abs(x), abs(y))
    
    # Longitud acumulada total acumulada JUSTO antes de empezar la capa actual (capa k-1)
    base_length = 4 * (k - 1) * k
    
    # El ancho de la pared de la capa actual es 2*k
    side = 2 * k
    
    # Caso 1: Pared Derecha (X fija en k, Y sube desde -k+1 hasta k)
    if x == k and y > -k:
        return base_length + (y - (-k + 1)) + 1
        
    # Caso 2: Pared Superior (Y fija en k, X se mueve hacia la izquierda desde k-1 hasta -k)
    elif y == k:
        return base_length + side + (k - x)
        
    # Caso 3: Pared Izquierda (X fija en -k, Y baja desde k-1 hasta -k)
    elif x == -k:
        return base_length + 2 * side + (k - y)
        
    # Caso 4: Pared Inferior (Y fija en -k, X se mueve a la derecha desde -k+1 hasta k)
    else: # y == -k
        return base_length + 3 * side + (x - (-k))