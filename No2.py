#Dita Widayanti Setiawan_F55121098_C TI

import time

# Graf dalam bentuk dictionary
graph = {
    'a': {'b': 12, 'c': 10, 'g': 12},
    'b': {'a': 12, 'd': 12, 'c': 8},
    'c': {'a': 10, 'b': 8, 'd': 11, 'e': 3, 'g': 9},
    'd': {'b': 12, 'c': 11, 'e': 11, 'f': 10},
    'e': {'c': 3, 'd': 11, 'f': 6, 'g': 7},
    'f': {'d': 10, 'e': 6, 'g': 9},
    'g': {'a': 12, 'c': 9, 'e': 7, 'f': 9}
}


def tsp(graph, start, visited, curr_path, min_path, curr_cost, num_nodes):
    if len(visited) == num_nodes and start in graph[curr_path[-1]]:
        curr_path.append(start)
        curr_cost += graph[curr_path[-2]][curr_path[-1]]
        if curr_cost < min_path['cost']:
            min_path['path'] = curr_path.copy()
            min_path['cost'] = curr_cost
        curr_path.pop()
        curr_cost -= graph[curr_path[-1]][start]
        return

    for node in graph[curr_path[-1]]:
        if node not in visited:
            curr_path.append(node)
            visited.add(node)
            curr_cost += graph[curr_path[-2]][node]

            tsp(graph, start, visited, curr_path, min_path, curr_cost, num_nodes)

            curr_path.pop()
            visited.remove(node)
            curr_cost -= graph[curr_path[-1]][node]


def tsp_main(graph):
    start = input("Masukkan titik awal: ").lower()

    if start not in graph:
        print("Titik awal tidak valid.")
        return

    num_nodes = len(graph)
    visited = set([start])
    curr_path = [start]
    min_path = {'path': [], 'cost': float('inf')}
    curr_cost = 0

    start_time = time.time()
    tsp(graph, start, visited, curr_path, min_path, curr_cost, num_nodes)
    end_time = time.time()

    print("\nHasil TSP (Traveling Salesman Problem):")
    print("Shortest path:", min_path['path'])
    print("Total cost:", min_path['cost'])
    print("Waktu komputasi:", end_time - start_time, "detik")


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_distance = float('inf')
        min_node = None

        for node in graph:
            if distances[node] < min_distance and node not in visited:
                min_distance = distances[node]
                min_node = node

        visited.add(min_node)

        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances


def dijkstra_main(graph):
    start = input("Masukkan titik awal: ").lower()

    if start not in graph:
        print("Titik awal tidak valid.")
        return

    start_time = time.time()
    shortest_distances = dijkstra(graph, start)
    end_time = time.time()

    print("\nHasil Dijkstra:")
    print("Titik awal:", start)
    for node, distance in shortest_distances.items():
        print("Titik", node, "- Jarak terpendek:", distance)

    print("Waktu komputasi:", end_time - start_time, "detik")


def main():
    print("Pilih algoritma:")
    print("1. TSP (Traveling Salesman Problem)")
    print("2. Dijkstra")

    choice = input("Masukkan pilihan (1/2): ")

    if choice == '1':
        tsp_main(graph)
    elif choice == '2':
        dijkstra_main(graph)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == '__main__':
    main()
