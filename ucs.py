import heapq

# Função para realizar a pesquisa de custo uniforme (UCS)
def ucs(grafo, inicio, objetivo):
    # Fila de prioridade para armazenar os nós a serem explorados (caminho de menor custo primeiro)
    fila_prioridade = [(0, inicio)]  # (custo_atual, nó)
    # Dicionário para rastrear os menores custos conhecidos para alcançar cada nó
    custos = {inicio: 0}
    # Dicionário para rastrear o caminho percorrido
    caminho = {inicio: None}

    while fila_prioridade:
        # Pega o nó com o menor custo acumulado
        custo_atual, no_atual = heapq.heappop(fila_prioridade)

        # Verifica se o nó atual é o objetivo
        if no_atual == objetivo:
            # Reconstrói o caminho percorrido até o objetivo
            caminho_final = []
            while no_atual is not None:
                caminho_final.append(no_atual)
                no_atual = caminho[no_atual]
            return caminho_final[::-1], custo_atual  # Retorna o caminho e o custo total

        # Expande os vizinhos do nó atual
        for vizinho, custo_vizinho in grafo[no_atual]:
            novo_custo = custo_atual + custo_vizinho
            # Se encontramos um caminho mais barato até o vizinho, atualizamos
            if vizinho not in custos or novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                heapq.heappush(fila_prioridade, (novo_custo, vizinho))
                caminho[vizinho] = no_atual

    # Retorna None se não houver caminho para o objetivo
    return None, float('inf')

# Exemplo de grafo com custos associados às arestas
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

# Executa o algoritmo UCS do nó 'A' até o nó 'F'
caminho, custo_total = ucs(grafo, 'A', 'F')

print(f"Caminho de menor custo: {caminho}")
print(f"Custo total: {custo_total}")
