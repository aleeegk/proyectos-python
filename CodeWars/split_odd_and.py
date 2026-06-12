def split_odd_and_even(n):
    # Convertimos el número a string para evaluar dígito por dígito
    s = str(n)
    result = []
    
    # Inicializamos el primer bloque con el primer dígito
    current_chunk = s[0]
    
    for digit in s[1:]:
        # Comparamos la paridad del dígito actual con el último del bloque
        # (int(A) % 2 == int(B) % 2) verifica si ambos son pares o ambos impares
        if int(digit) % 2 == int(current_chunk[-1]) % 2:
            current_chunk += digit
        else:
            # Si cambia la paridad, guardamos el bloque anterior y empezamos uno nuevo
            result.append(int(current_chunk))
            current_chunk = digit
            
    # No olvides agregar el último bloque que quedó en proceso
    result.append(int(current_chunk))
    
    return result