# README – Path Planning & Graph Algorithms (Assignment 3)

**Name:** Moola Goutham Reddy  
**Roll No:** SE24UCSE243  

---

## Overview
This project contains implementations of three important algorithms related to path finding and graph traversal:

1. **Dijkstra’s Algorithm** – to find shortest distances between Indian cities  
2. **Grid-based Path Planning (A\*)** – for navigating a robot in a grid with obstacles  
3. **Dynamic UGV Path Planning** – handling dynamic environments and obstacle updates  

The goal of this assignment is to understand how shortest path algorithms work in both real-world maps and simulated environments.

---

## 1. Dijkstra’s Algorithm (Cities Dataset)

- A graph of Indian cities is created using a CSV file (`india_cities.csv`)  
- Each city is treated as a node, and distances between them are edges  
- The algorithm finds the shortest distance from a given starting city to all other cities  

### Key Idea
Always choose the node with the minimum distance using a **priority queue**.


---

## 2. Grid-Based Path Planning (A\* Algorithm)

- A **70×70 grid** is generated  
- Cells represent:
  - `0` → Free space  
  - `1` → Obstacles  
- The A\* algorithm finds the shortest path from:
  - Start → Top-left  
  - Goal → Bottom-right  

### Why A\*?
It is faster than BFS because it uses a **heuristic (Manhattan distance)** to guide the search.

---

## 3. Dynamic UGV Path Planning

- Simulates a robot moving in a **dynamic environment**  
- Obstacles can change during execution  
- The algorithm updates the path accordingly  

---

## Visualization

The grid is displayed using **matplotlib** for better understanding.

---
