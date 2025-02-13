from collections import deque


def bfs(graph, start_node):
    visited = set()  # Conjunto para rastrear nós visitados
    queue = deque([start_node])  # Fila iniciada com o nó inicial

    while queue:
        # Remove o primeiro nó da fila
        current_node = queue.popleft()

        # Se ainda não foi visitado, processa e marca como visitado
        if current_node not in visited:
            print(current_node)  # Imprime ou processa o nó
            visited.add(current_node)

            # Adiciona todos os vizinhos do nó atual que ainda não foram visitados
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Exemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Chamando o BFS a partir do nó 'A'
bfs(graph, 'A')
