## Project Description
This repository showcases solutions to fundamental **Artificial Intelligence problems** modeled as **Constraint Satisfaction Problems (CSPs)**. The focus is on representing problems with variables, domains, and constraints, and solving them using an efficient **backtracking search strategy**.

The project covers multiple real-world and logical scenarios, demonstrating how constraints can be systematically applied to reach correct solutions.

---

### Australia Map Coloring
* Assigns colors to major regions of Australia 
* Regions involved: WA, NT, Queensland, SA, NSW, V, T 
* Rule: Adjacent regions cannot have the same color 
* Method used: Recursive backtracking with constraint checking 

---

### Telangana District Coloring
* Applies graph coloring to all 33 districts of Telangana
* Uses a predefined adjacency relationship between districts
* Rule: No two neighboring districts share the same color
* Includes a graphical output using Python visualization tools

---

### Sudoku Puzzle Solver
* Solves a 9×9 Sudoku puzzle automatically 
* Empty cells are represented using `0` 
* Rules enforced:
  * Each row contains unique digits (1–9)
  * Each column contains unique digits (1–9)
  * Each 3×3 box contains unique digits (1–9) 
* Technique: Depth-first search with backtracking 

---

### Cryptarithmetic Problem
* Solves the equation: 
  **SEND + MORE = MONEY** 
* Rules:
  * Each character represents a distinct digit 
  * Leading characters cannot be zero 
  * The arithmetic equation must hold true 
* Output example: 
  9567 + 1085 = 10652 

---

## Tools & Environment
* Programming Language: Python 3 
* External Library:
  * matplotlib (for visual representation)

---

## Learning Outcomes
* Understanding of Constraint Satisfaction Problems
* Implementation of backtracking algorithms 
* Handling constraints in different problem domains 
* Graph-based problem modeling 
* Logical reasoning and search techniques 

---
