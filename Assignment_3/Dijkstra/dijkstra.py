import csv
import heapq

INF = 100000.0

def load_graph(filename):
    graph = {}

    with open(filename, 'r') as file:
        data = list(csv.reader(file))

    cities = data[0][1:]

    for i in range(1, len(data)):
        city = data[i][0]
        graph[city] = {}

        for j in range(1, len(data[i])):
            d = float(data[i][j])

            if d != INF and i != j:
                graph[city][cities[j-1]] = d

    return graph

def dijkstra(graph, start):
    dist = {c: float('inf') for c in graph}
    parent = {c: None for c in graph}

    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        for v, w in graph[u].items():
            if d + w < dist[v]:
                dist[v] = d + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parent

def get_path(parent, end):
    path = []
    while end:
        path.append(end)
        end = parent[end]
    return path[::-1]

if __name__ == "__main__":
    graph = load_graph("india_cities.csv")

    start = input("Enter start city: ")
    end = input("Enter destination city: ")

    if start not in graph or end not in graph:
        print("Invalid city name!")
    else:
        dist, parent = dijkstra(graph, start)
        path = get_path(parent, end)

        print("\nShortest Path:")
        print(" -> ".join(path))

        print("\nTotal Distance:")
        print(f"{dist[end]:.2f} km")
