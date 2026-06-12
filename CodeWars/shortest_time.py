def shorterest_time(n, m, speeds):
    if n == 0:
        return 0
    
    a, b, c, d = speeds
    min_time = n * d  # Opción base: bajar caminando por completo
    
    # John podría caminar hasta un piso intermedio 'f' y tomar el ascensor allí
    for f in range(n + 1):
        walk_time = abs(n - f) * d
        elevator_travel = abs(m - f) * a + f * a
        elevator_doors = b + c + b
        
        total = walk_time + elevator_travel + elevator_doors
        if total < min_time:
            min_time = total
            
    return min_time