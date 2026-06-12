import math

def find_number(sums):
    # La lista de 'sums' contiene los pares sumados en un orden estrictamente definido:
    # d0+d1, d0+d2, ..., d0+d_(k-1), d1+d2, d1+d3, ..., d_(k-2)+d_(k-1)
    # Es decir, itera exactamente de la forma: for i in range(k): for j in range(i+1, k)
    
    n = len(sums)
    k = int((1 + math.sqrt(1 + 8 * n)) // 2)

    # Inicializamos una lista de dígitos vacía para el Backtracking
    digits = [None] * k

    def backtrack(idx):
        if idx == k:
            return True

        # El primer dígito no puede ser 0
        start_digit = 1 if idx == 0 else 0

        for d in range(start_digit, 10):
            digits[idx] = d
            
            # Validación inmediata sobre la marcha:
            # Cada vez que asignamos el dígito en la posición 'idx', podemos verificar
            # todas las sumas que involucran a este dígito con los dígitos anteriores (i < idx).
            valid = True
            for i in range(idx):
                # Calculamos el índice exacto que tendría la suma de digits[i] y digits[idx]
                # en la lista plana original 'sums' basada en el orden de los bucles anidados.
                actual_sums_index = (i * (2 * k - i - 1)) // 2 + (idx - i - 1)
                
                if digits[i] + digits[idx] != sums[actual_sums_index]:
                    valid = False
                    break
            
            if valid:
                if backtrack(idx + 1):
                    return True
                    
        return False

    if backtrack(0):
        return int("".join(map(str, digits)))
    return 0