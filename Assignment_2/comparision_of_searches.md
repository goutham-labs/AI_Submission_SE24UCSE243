# Comparision Of All Variants of Uninformed Search 
## (Missionaries and Cannibals Problem)

Uninformed search strategies explore the state space without using any heuristic or domain-specific knowledge. In this analysis, different uninformed search algorithms were applied to the Missionaries and Cannibals problem and evaluated based on their theoretical properties and practical performance.

---

## 1. Breadth First Search (BFS)

Breadth First Search is a blind search strategy that explores the state space level by level. It expands all nodes at a given depth before proceeding to the next depth level. BFS uses a **queue (FIFO structure)** for node expansion.

### Properties

- **Completeness:** Yes. It guarantees finding a solution if one exists.
- **Optimality:** Yes, when all step costs are equal.
- **Time Complexity:** `O(b^d)`
- **Space Complexity:** `O(b^d)` (can be significantly large)

Where:

- `b` = branching factor 
- `d` = depth of the shallowest solution 

### Observations in This Problem

In the Missionaries and Cannibals problem, BFS successfully found a valid solution and ensured the shortest possible sequence of moves. However, it required storing a large number of intermediate states in memory, resulting in high memory consumption.

---

## 2. Depth First Search (DFS)

Depth First Search explores as deeply as possible along a branch before backtracking. It uses a **stack (LIFO structure)** for node expansion.

### Properties

- **Completeness:** Not guaranteed in infinite-depth state spaces.
- **Optimality:** No. It does not ensure the shortest path.
- **Time Complexity:** `O(b^m)`
- **Space Complexity:** `O(bm)` (lower than BFS)

Where:

- `m` = maximum depth of the search tree

### Observations in This Problem

DFS was able to reach the goal state successfully. However, the solution path differed from that obtained using BFS and was not necessarily optimal. Although DFS required less memory compared to BFS, it may explore unnecessary deep paths before reaching the solution.

---

## 3. Depth Bounded Depth First Search (DBDFS)

Depth Bounded DFS is a variation of DFS in which the search is restricted to a predefined depth limit. Nodes beyond this limit are not expanded.

### Properties

- Prevents infinite exploration.
- Reduces unnecessary deep traversal.
- **Completeness:** Only if the depth limit ≥ solution depth.
- **Optimality:** No.

### Observations in This Problem

When the depth limit was set lower than the actual solution depth, the algorithm failed to find the goal state. The solution was found only when the limit was increased sufficiently. Therefore, DBDFS heavily depends on selecting an appropriate depth bound.

---

## 4. Depth First Iterative Deepening (DFID / IDS)

Depth First Iterative Deepening combines the advantages of BFS and DFS. It performs repeated depth-limited searches with increasing depth limits until the solution is found.

### Properties

- **Completeness:** Yes.
- **Optimality:** Yes (for uniform step costs).
- **Time Complexity:** `O(b^d)`
- **Space Complexity:** `O(bd)` (similar to DFS)

### Observations in This Problem

DFID successfully found the same optimal solution as BFS. It required significantly less memory compared to BFS while still guaranteeing optimality. Additionally, it avoided the infinite-depth problems associated with standard DFS.

---

## Conclusion

From the above analysis, it is evident that each uninformed search strategy has its own strengths and limitations. BFS guarantees optimality but consumes high memory. DFS is memory-efficient but does not guarantee optimality. DBDFS provides controlled exploration but depends on the correct selection of depth limit. DFID offers a balanced approach by ensuring optimality while maintaining reasonable memory usage.

For the Missionaries and Cannibals problem, **Depth First Iterative Deepening** proved to be the most efficient approach when both optimality and memory efficiency were considered.
