from collections import deque

def cogsebi(gears, connections, driver_id, driver_rpm):
    n = len(gears)
    # Inicializamos todos los engranajes desconectados a 0.0
    rpms = [0.0] * n
    
    # 1. Construir la lista de adyacencia del grafo de conexiones
    adj = [[] for _ in range(n)]
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)
        
    # 2. Configurar el engranaje motor (Driver)
    rpms[driver_id] = float(driver_rpm)
    
    # Cola para BFS: almacena el ID del engranaje actual
    queue = deque([driver_id])
    
    # Conjunto de visitados para evitar ciclos infinitos en redes complejas
    visited = {driver_id}
    
    # 3. Propagación de RPMs por BFS
    while queue:
        curr = queue.popleft()
        curr_rpm = rpms[curr]
        curr_teeth = gears[curr]
        
        for neighbor in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                
                # REGLAS DE ENGRANAJE:
                # - Relación de velocidad: RPM_B = RPM_A * (Teeth_A / Teeth_B)
                # - Cambio de dirección: Multiplicamos por -1 porque el sentido se invierte
                neighbor_teeth = gears[neighbor]
                rpms[neighbor] = curr_rpm * (curr_teeth / neighbor_teeth) * -1.0
                
                queue.append(neighbor)
                
    return rpms