from collections import deque

# Função para realizar a pesquisa em largura (BFS)
def bfs(grafo, inicial):
    # Cria uma fila para controlar os nós a serem visitados
    fila = deque([inicial])
    # Cria um conjunto para rastrear os nós que já foram visitados
    visitados = set([inicial])
    
    # Enquanto houver nós na fila
    while fila:
        # Remove o primeiro nó da fila
        no_atual = fila.popleft()
        print(f"Visitando nó: {no_atual}")
        
        # Para cada vizinho do nó atual
        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                # Marca como visitado e adiciona na fila
                visitados.add(vizinho)
                fila.append(vizinho)

# Exemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Chamando a função BFS a partir do nó 'A'
bfs(grafo, 'A')
