import heapq

def dijkstra(graph, start):
    # Afstanden initialiseren met "oneindig"
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue: (afstand, knoop)
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Sla over als we al een kortere route hadden
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Kortere route gevonden
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Voorbeeldgraaf (gerichte graaf met gewichten)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {'F': 3},
    'F': {}
}

# De voorbeeldgraaf uitprinten
print()
print("De ingevoerde voorbeeldgraaf is:")
print(graph)

# Run het algoritme vanaf knoop 'A'
start_node = 'A'
result = dijkstra(graph, start_node)

# Netjes uitprinten
print(f"\nKortste afstanden vanaf knoop '{start_node}':")
for node in sorted(result):
    afstand = result[node]
    if afstand == float('inf'):
        print(f" - {node}: geen pad bereikbaar")
    else:
        print(f" - {node}: {afstand}")
