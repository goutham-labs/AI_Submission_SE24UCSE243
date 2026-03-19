#!/usr/bin/env python3

"""
UGV Navigation using A*
"""

import random
import heapq
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

GRID_DIM = 70
OBSTACLE_PROB = 0.18

SOURCE = (0, 0)
TARGET = (GRID_DIM - 1, GRID_DIM - 1)


# Heuristic Function
def estimate_cost(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# A* Search Function
def find_route(field, origin, destination):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    priority_queue = []
    heapq.heappush(priority_queue, (0, origin))

    parent_map = {}
    travel_cost = {origin: 0}

    explored_nodes = 0
    start_clock = time.time()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)[1]
        explored_nodes += 1

        if current_node == destination:
            end_clock = time.time()
            final_path = build_path(parent_map, origin, destination)
            return final_path, explored_nodes, end_clock - start_clock

        cx, cy = current_node

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            neighbor = (nx, ny)

            if not (0 <= nx < GRID_DIM and 0 <= ny < GRID_DIM):
                continue

            if field[nx][ny] == 1:
                continue

            updated_cost = travel_cost[current_node] + 1

            if neighbor not in travel_cost or updated_cost < travel_cost[neighbor]:
                travel_cost[neighbor] = updated_cost
                priority = updated_cost + estimate_cost(neighbor, destination)

                heapq.heappush(priority_queue, (priority, neighbor))
                parent_map[neighbor] = current_node

    return None, explored_nodes, time.time() - start_clock

def build_path(parent_map, origin, destination):
    node = destination
    route = [node]

    while node != origin:
        node = parent_map[node]
        route.append(node)

    route.reverse()
    return route

def create_environment():
    while True:
        terrain = [[0 for _ in range(GRID_DIM)] for _ in range(GRID_DIM)]

        for i in range(GRID_DIM):
            for j in range(GRID_DIM):
                if random.random() < OBSTACLE_PROB:
                    terrain[i][j] = 1

        terrain[SOURCE[0]][SOURCE[1]] = 0
        terrain[TARGET[0]][TARGET[1]] = 0

        route, _, _ = find_route(terrain, SOURCE, TARGET)

        if route:
            return terrain, route

def display_map(terrain, route):
    visual = np.array(terrain)

    for r, c in route:
        visual[r][c] = 2

    color_scheme = ListedColormap(['white', 'black', 'red'])

    plt.figure(figsize=(10,10), dpi=150)
    plt.imshow(visual, cmap=color_scheme, interpolation='nearest')

    y_coords = [c for r, c in route]
    x_coords = [r for r, c in route]

    plt.plot(y_coords, x_coords, linewidth=2)
    plt.scatter(SOURCE[1], SOURCE[0], s=80, label='Start')
    plt.scatter(TARGET[1], TARGET[0], s=80, label='Goal')

    plt.grid(color='gray', linestyle='-', linewidth=0.2)
    plt.title("UGV Path Planning using A*")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    env, route = create_environment()

    route, visited, runtime = find_route(env, SOURCE, TARGET)

    print("\n=== OUTPUT ===")
    print("Path successfully found!")
    print("Total steps:", len(route))
    print("Nodes explored:", visited)
    print("Execution time:", round(runtime, 5), "seconds")

    display_map(env, route)
