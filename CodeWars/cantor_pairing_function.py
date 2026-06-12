def cantor(n):
    # 1. Encontrar en qué diagonal se encuentra el n-ésimo elemento
    # Una diagonal 'd' contiene 'd' elementos. La suma de elementos hasta la diagonal d
    # viene dada por la fórmula triangular: d * (d + 1) // 2
    d = 1
    total_elements = 0
    
    # Buscamos la diagonal d más pequeña tal que los elementos acumulados cubran n
    # Para n grandes, esto toma O(sqrt(n)) pasos, lo cual es instantáneo para n = 268435455
    while total_elements + d < n:
        total_elements += d
        d += 1
        
    # 2. Calcular la posición exacta (índice) dentro de esa diagonal d
    # El índice va desde 1 hasta d
    index_in_diagonal = n - total_elements
    
    # 3. Determinar el numerador y denominador basándonos en la dirección de la diagonal
    if d % 2 == 0:
        # Diagonal par: empieza en 1/d y va hacia d/1 (num aumenta, den disminuye)
        num = index_in_diagonal
        den = d - index_in_diagonal + 1
    else:
        # Diagonal impar: empieza en d/1 y va hacia 1/d (num disminuye, den aumenta)
        num = d - index_in_diagonal + 1
        den = index_in_diagonal
        
    return f"{num}/{den}"