import itertools

def solve_puzzle(clues):
    N = 7
    
    def count_visible(line):
        visible, max_height = 0, 0
        for h in line:
            if h > max_height:
                visible += 1
                max_height = h
        return visible

    # 1. Precalcular todas las permutaciones y mapearlas por pistas
    all_perms = list(itertools.permutations(range(1, N + 1)))
    valid_lines = {(i, j): [] for i in range(N + 1) for j in range(N + 1)}
    for perm in all_perms:
        v_left = count_visible(perm)
        v_right = count_visible(perm[::-1])
        for l_clue in (v_left, 0):
            for r_clue in (v_right, 0):
                valid_lines[(l_clue, r_clue)].append(perm)

    # 2. Mapeo correcto de pistas de CodeWars
    row_clues = [(clues[27 - i], clues[7 + i]) for i in range(N)]
    col_clues = [(clues[i], clues[20 - i]) for i in range(N)]

    # 3. Filtrar conjuntos de permutaciones candidatas por cada línea
    row_candidates = [list(valid_lines[row_clues[r]]) for r in range(N)]
    col_candidates = [list(valid_lines[col_clues[c]]) for c in range(N)]

    # 4. Propagación de restricciones fuerte (Filtra a nivel de línea completa continuamente)
    changed = True
    while changed:
        changed = False
        
        # Filtrar filas usando columnas válidas
        for r in range(N):
            c_allowed = [set(col[r] for col in col_candidates[c]) for c in range(N)]
            new_rows = [row for row in row_candidates[r] if all(row[c] in c_allowed[c] for c in range(N))]
            if len(new_rows) != len(row_candidates[r]):
                row_candidates[r] = new_rows
                changed = True
                
        # Filtrar columnas usando filas válidas
        for c in range(N):
            r_allowed = [set(row[c] for row in row_candidates[r]) for r in range(N)]
            new_cols = [col for col in col_candidates[c] if all(col[r] in r_allowed[r] for r in range(N))]
            if len(new_cols) != len(col_candidates[c]):
                col_candidates[c] = new_cols
                changed = True

    # 5. Inicializar estructuras de backtracking rápido
    grid = [[0] * N for _ in range(N)]
    col_used = [[False] * (N + 1) for _ in range(N)]

    # 6. Backtracking por FILA COMPLETA usando la heurística de la fila con menos candidatos
    def backtrack(filled_mask):
        if filled_mask == (1 << N) - 1:
            return True

        # Encontrar la fila sin rellenar que tenga menos permutaciones posibles
        best_r = -1
        min_options = 9999
        for r in range(N):
            if not (filled_mask & (1 << r)):
                num_options = len(row_candidates[r])
                if num_options < min_options:
                    min_options = num_options
                    best_r = r

        if best_r == -1:
            return False

        r = best_r
        # Intentar colocar cada permutación válida restante para esta fila
        for row in row_candidates[r]:
            # Verificar colisiones verticales en O(1) con la matriz booleana
            legal = True
            for c in range(N):
                if col_used[c][row[c]]:
                    legal = False
                    break
            if not legal:
                continue

            # Colocar fila de forma tentativa
            grid[r] = list(row)
            for c in range(N):
                col_used[c][row[c]] = True

            if backtrack(filled_mask | (1 << r)):
                return True

            # Deshacer
            for c in range(N):
                col_used[c][row[c]] = False

        return False

    backtrack(0)
    return grid