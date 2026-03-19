#!/usr/bin/env python3

import heapq
import random
import time
import math
import copy

ROWS = 70
COLS = 70
EMPTY = 0
WALL = 1
VISION = 5
DYNAMIC_RATE = 0.03
INF = float('inf')


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


MOVES = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
    (-1, -1), (-1, 1),
    (1, -1), (1, 1)
]


def get_neighbors(x, y):
    neighbors = []
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROWS and 0 <= ny < COLS:
            neighbors.append((nx, ny))
    return neighbors


# ---------------- D* Lite ---------------- #

class DStarLite:

    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

        self.g = {}
        self.rhs = {}

        self.U = []
        self.km = 0

        for i in range(ROWS):
            for j in range(COLS):
                self.g[(i, j)] = INF
                self.rhs[(i, j)] = INF

        self.rhs[goal] = 0
        heapq.heappush(self.U, (self.calculate_key(goal), goal))


    def calculate_key(self, node):
        return (min(self.g[node], self.rhs[node]) + heuristic(self.start, node) + self.km,
                min(self.g[node], self.rhs[node]))


    def update_vertex(self, u):
        if u != self.goal:
            self.rhs[u] = min(
                [self.g[s] + 1 for s in get_neighbors(u[0], u[1]) if self.grid[s[0]][s[1]] != WALL] or [INF]
            )

        self.U = [(k, n) for (k, n) in self.U if n != u]
        heapq.heapify(self.U)

        if self.g[u] != self.rhs[u]:
            heapq.heappush(self.U, (self.calculate_key(u), u))


    def compute_shortest_path(self):
        while self.U:
            k_old, u = heapq.heappop(self.U)

            if self.g[u] > self.rhs[u]:
                self.g[u] = self.rhs[u]
                for s in get_neighbors(u[0], u[1]):
                    self.update_vertex(s)
            else:
                self.g[u] = INF
                self.update_vertex(u)
                for s in get_neighbors(u[0], u[1]):
                    self.update_vertex(s)


    def get_path(self):
        path = [self.start]
        current = self.start

        while current != self.goal:
            neighbors = get_neighbors(current[0], current[1])
            current = min(
                neighbors,
                key=lambda x: self.g[x] if self.grid[x[0]][x[1]] != WALL else INF
            )
            if self.g[current] == INF:
                return []
            path.append(current)

        return path

class DynamicUGV:

    def __init__(self, real_map, start, goal):
        self.real_map = real_map
        self.start = start
        self.goal = goal
        self.pos = start

        self.known_map = [[EMPTY]*COLS for _ in range(ROWS)]
        self.path = []

        self.steps = 0
        self.replans = 0
        self.distance = 0


    def sense(self):
        r, c = self.pos
        changed = False

        for i in range(max(0, r-VISION), min(ROWS, r+VISION+1)):
            for j in range(max(0, c-VISION), min(COLS, c+VISION+1)):
                if self.real_map[i][j] == WALL and self.known_map[i][j] == EMPTY:
                    self.known_map[i][j] = WALL
                    changed = True

        return changed


    def add_dynamic_obstacles(self):
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in [self.start, self.goal, self.pos]:
                    if self.real_map[i][j] == EMPTY:
                        if random.random() < (DYNAMIC_RATE / (ROWS*COLS)) * 100:
                            self.real_map[i][j] = WALL


    def move(self):
        if len(self.path) < 2:
            return False

        next_pos = self.path[1]
        self.distance += 1
        self.pos = next_pos
        self.path = self.path[1:]
        self.steps += 1

        return True


    def run(self):
        print("D* Lite UGV Simulation Started")

        dstar = DStarLite(self.known_map, self.pos, self.goal)
        dstar.compute_shortest_path()
        self.path = dstar.get_path()

        start_time = time.time()

        while self.pos != self.goal:

            if not self.path:
                print("No path available")
                return False

            self.move()

            changed = self.sense()

            if changed:
                self.replans += 1
                dstar = DStarLite(self.known_map, self.pos, self.goal)
                dstar.compute_shortest_path()
                self.path = dstar.get_path()

            self.add_dynamic_obstacles()

        end_time = time.time()

        print("\nReached Goal!")
        print("Steps:", self.steps)
        print("Distance:", self.distance)
        print("Replans:", self.replans)
        print("Time:", round((end_time - start_time)*1000, 2), "ms")

        return True

if __name__ == "__main__":

    random.seed(42)

    base_map = []
    for _ in range(ROWS):
        row = []
        for _ in range(COLS):
            if random.random() < 0.2:
                row.append(WALL)
            else:
                row.append(EMPTY)
        base_map.append(row)

    start = (2, 2)
    goal = (67, 67)

    base_map[start[0]][start[1]] = EMPTY
    base_map[goal[0]][goal[1]] = EMPTY

    ugv = DynamicUGV(copy.deepcopy(base_map), start, goal)
    ugv.run()
