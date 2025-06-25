def bfs_min_path(graph, start):
    # Distanze minime dal nodo di partenza
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}

    dist[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[current] + 1
                prev[neighbor] = current
                queue.append(neighbor)

    return dist, prev

def reconstruct_path(prev, start, target):
    path = []
    at = target
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()
    return path if path[0] == start else []

# 🔧 Esempio di uso:
if __name__ == "__main__":
    # Grafo rappresentato come dizionario di adiacenza
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D', 'E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }

    start = 'A'
    target = 'F'

    dist, prev = bfs_min_path(graph, start)
    path = reconstruct_path(prev, start, target)

    print(f"Distanze minime da {start}:", dist)
    print(f"Percorso minimo da {start} a {target}:", path)
📌 Output atteso:
arduino
Copia
Modifica
Distanze minime da A: {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 3}
Percorso minimo da A a F: ['A', 'B', 'D', 'F']
 # bfs per cammino mino tra due nodi


def getShortestPath(self, u, v):
    return nx.single_source_dijkstra(self._grafo, u, v)
# dijkstra tra nodo 1 e nodo 2, cammino peso minimo