# Função para realizar a pesquisa em profundidade (DFS) de forma recursiva
def dfs(grafo, no, visitados=None):
    if visitados is None:
        visitados = set()
    
    # Marca o nó atual como visitado
    visitados.add(no)
    print(f"Visitando nó: {no}")
    
    # Para cada vizinho do nó atual, faz uma chamada recursiva se ainda não foi visitado
    for vizinho in grafo[no]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)
    
    return visitados

# Exemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Chamando a função DFS a partir do nó 'A'
dfs(grafo, 'A')
