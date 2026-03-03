# AI_Submission_SE24UCSE243

# Uninformed Search Algorithms

This module contains the implementation of **Uninformed (Blind) Search Algorithms** used in Artificial Intelligence.

Uninformed search algorithms explore the state space without using heuristics or additional domain knowledge. They rely only on the problem definition such as the initial state, goal state, and successor function.

Uninformed search strategies systematically explore nodes in a search tree until a goal state is found.

### Algorithms Implemented
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- (Add others if included in your code)

## Key Concepts

- **State Space** – All possible states of the problem  
- **Initial State** – Starting point of the search  
- **Goal State** – Target state to reach  
- **Frontier (Open List)** – Nodes yet to be explored  
- **Explored Set (Closed List)** – Nodes already visited  

## Working Principle

1. Start from the initial node.
2. Expand nodes based on the selected search strategy.
3. Continue exploring until the goal state is found.
4. Return the solution path (if exists).

## How to Run (Make sure python3 is installed)

python3 uninformed_search.py

## Sample Output
![uninformed_searches](https://github.com/user-attachments/assets/a6682952-03ff-4284-b8c0-785d2e3400e4)

# Turing Test Simulation

This module presents a simplified implementation and conceptual architecture of the **Turing Test**, proposed by Alan Turing.

The Turing Test evaluates whether a machine can imitate human responses well enough that a human evaluator cannot reliably distinguish it from a real human.

In this implementation:

- A human evaluator interacts with two participants.
- One participant is a human.
- The other participant is a machine (AI system).
- The evaluator must determine which one is the machine.

The system hides identities and processes responses through an interface layer.

## Key Concepts

- Human vs Machine Interaction  
- Natural Language Simulation  
- Identity Masking  
- Response Evaluation  

## Architecture Components

- **User Interface** – Handles input/output  
- **Human Participant** – Simulated human responses  
- **Machine Participant** – AI-generated responses  
- **Evaluator Logic** – Determines indistinguishability  

## How to Run (Make sure Python 3 is installed)

python3 demo_tt.py

## Sample Output
![tt](https://github.com/user-attachments/assets/5bb05972-4ab0-48ed-b3f0-27be2f5353f5)

# CAPTCHA System Implementation

This module demonstrates a basic implementation of a **CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart)** system.

CAPTCHA is used to differentiate between human users and automated bots.

The system generates a challenge that:

- Is easy for humans to solve  
- Is difficult for automated programs (bots)  
- Verifies user input against the correct response  

## Key Concepts

- Human Verification  
- Bot Prevention  
- Random Challenge Generation  
- Input Validation  

## Architecture Components

- **Challenge Generator** – Creates CAPTCHA text/problem  
- **Display Layer** – Shows CAPTCHA to user  
- **User Input Handler** – Collects response  
- **Verification Module** – Checks correctness  

## How to Run (Make sure python3 is installed)
python3 demo_captcha.py

## Sample Output
![captcha](https://github.com/user-attachments/assets/02b2a92f-cab3-4426-9076-12f87c364132)
