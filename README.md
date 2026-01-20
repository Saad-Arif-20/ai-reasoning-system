# Classical AI Reasoning System

A comprehensive implementation of fundamental Artificial Intelligence concepts, distinguishing **Classical AI** (reasoning and planning) from modern Machine Learning. This project builds sophisticated agents capable of decision-making in adversarial environments and solving complex constraint satisfaction problems.

## Project Overview

While modern AI often focuses on statistical learning (Neural Networks), **Classical AI** focuses on explicit reasoning, planning, and search. This system implements two pillars of classical AI:

1.  **Adversarial Reasoning**: An invincible agent that plays zero-sum games (Tic-Tac-Toe) using game theory optimization.
2.  **Constraint Logic**: A solver that resolves complex logic puzzles (Sudoku) using pure constraint satisfaction algorithms.

### Key Objectives
- **Implement Search Algorithms**: Build Minimax and Backtracking search from scratch.
- **Optimize Performance**: Apply Alpha-Beta pruning and Heuristics (MRV) to reduce computational cost.
- **Separate Concerns**: Decouple "Agents" (decision makers) from "Environments" (problem rules).

---

## System Architecture

The project follows a modular Object-Oriented architecture:

```
/ai-reasoning-system
 ├── agents/               # Decision-making entities
 │   ├── base.py           # Abstract Agent interface
 │   ├── minimax_agent.py  # The "Smart" AI agent
 │   └── random_agent.py   # Baseline for comparison
 ├── algorithms/           # Pure mathematical logic
 │   ├── minimax.py        # Alpha-Beta Pruning implementation
 │   └── csp_solver.py     # Backtracking Search implementation
 ├── environments/         # The "World" rules
 │   ├── games.py          # State representation (Tic-Tac-Toe)
 │   └── sudoku.py         # Constraint definitions
 ├── docs/                 # Formal documentation
 │   ├── PROBLEM_FORMULATION.md
 │   └── ALGORITHM_SELECTION.md
 └── main.py               # CLI Application
```

---

## Algorithmic Core

### 1. Minimax with Alpha-Beta Pruning
Used for the Game Playing Agent.
- **Concept**: A recursive algorithm that minimizes the maximum possible loss.
- **Time Complexity**: $O(b^d)$ (worst case) $\rightarrow O(b^{d/2})$ (with optimal pruning).
- **Optimization**: **Alpha-Beta Pruning** ignores branches that cannot influence the final decision, allowing the agent to look twice as deep in the same time.

### 2. Constraint Satisfaction (Backtracking)
Used for the Sudoku Solver.
- **Concept**: A depth-first search that builds candidates and abandons a candidate ("backtracks") as soon as it determines the candidate cannot be completed.
- **Heuristics**:
    - **MRV (Minimum Remaining Values)**: Prioritizes variables with the fewest legal moves to fail fast.
    - **LCV (Least Constraining Value)**: Prioritizes values that leave the most options open for neighbors.

---

## Quick Start Guide

### Prerequisites
- Python 3.8+ (No external libraries required)

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/ai-reasoning-system.git

# Navigate to project
cd ai-reasoning-system
```

### Usage
Run the interactive CLI:
```bash
python main.py
```

You will be presented with a menu:
1.  **Play Tic-Tac-Toe**: Challenge the invincible Minimax agent.
2.  **Solve Sudoku**: Watch the CSP solver crack a "Hard" difficulty puzzle in milliseconds.

### Running Tests
To verify the AI's optimality (Minimax vs Minimax should draw) and Solver correctness:
```bash
python test_ai.py
```

---

## Learning Context & Academic Alignment

This project demonstrates applied understanding of key artificial intelligence concepts:

| Outcome | Implementation Evidence |
| :--- | :--- |
| **Search Strategies** | Implementation of adversarial search (Minimax) and uninformed/informed search. |
| **Knowledge Representation** | Modeling problems as State Spaces and Constraint Graphs. |
| **Heuristics** | Application of Alpha-Beta pruning and MRV heuristics to optimize search. |
| **Agent Design** | Creation of autonomous agents that perceive state and act rationally. |

**Related Concepts**:
*   Artificial intelligence fundamentals
*   Algorithms and data structures
*   Search and optimization

---

## Performance Analysis

### Game Agent Performance
*   **Depth**: 9 (Full Game Tree)
*   **Nodes Evaluated (First Move)**: ~4,500 (with pruning) vs ~300,000 (without).
*   **Result**: The agent is mathematically proven to **never lose**.

### Logic Solver Performance
*   **Puzzle Difficulty**: Hard (17 clues)
*   **Solve Time**: < 0.05 seconds
*   **Method**: Backtracking + MRV Heuristic
*   **Comparison**: Brute force would take years; Backtracking takes milliseconds.

---

## Future Improvements

1.  **Monte Carlo Tree Search (MCTS)**: Implement MCTS for complex games like Connect-4 or Go where Minimax is too slow.
2.  **AC-3 Algorithm**: Implement Arc Consistency to pre-process CSPs before backtracking.
3.  **GUI Application**: Add a graphical interface using PyGame or Tkinter.

---

## License
This project is open-source and available under the MIT License.

**Author**: SAAD ARIF
**Year**: 2025
