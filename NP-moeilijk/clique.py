from itertools import combinations

def is_clique(graph, nodes):
    """Controleer of elke node in 'nodes' met elke andere verbonden is."""
    for u, v in combinations(nodes, 2):
        if v not in graph[u]:
            return False
    return True

def bevat_k_clique(graph, k):
    """Controleer of de graaf een clique van grootte k bevat."""
    nodes = list(graph.keys())
    for subset in combinations(nodes, k):
        if is_clique(graph, subset):
            return True, subset
    return False, None

# Voorbeeld invoer (adjacency list)
graaf = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C'],
    'E': ['F'],
    'F': ['E']
}

k = 4

heeft_clique, knopen = bevat_k_clique(graaf, k)
if heeft_clique:
    print(f"Ja, er is een clique van grootte {k}: {knopen}")
else:
    print(f"Nee, er is geen clique van grootte {k}")
