# AI Algorithm Selection & Analysis

## 1. Game Playing: Minimax vs. Others

### Why Minimax?
For a deterministic, perfect-information game like Tic-Tac-Toe (and Checkers/Chess/Go), **Minimax** is the theoretically optimal strategy.

| Algorithm | Suitability | Reasoning |
| :--- | :--- | :--- |
| **Random** | Low | Cannot guarantee a win or draw. |
| **Rule-Based** | Medium | "If 2 in a row, block". Prone to edge cases and hard to maintain. |
| **BFS/DFS** | Low | Finds paths, but assumes opponent does nothing. Fails in adversarial settings. |
| **Minimax** | **High** | Assumes optimal opponent play. Guarantees non-losing strategy for Tic-Tac-Toe. |
| **Reinforcement Learning**| High (Overkill) | Q-Learning works but requires thousands of training episodes. Minimax solves it instantly. |

### Optimization: Alpha-Beta Pruning
Standard Minimax explores $O(b^d)$ nodes. For depth 9, this is manageable ($~3 \times 10^5$), but for complex games it fails.
*   **Technique**: We maintain `alpha` (best max found) and `beta` (best min found).
*   **Result**: If we find a move worse than a previously known option, we stop searching that branch.
*   **Efficiency**: Reduces effective branching factor from $b$ to $\sqrt{b}$ in best case. Allows searching twice as deep.

---

## 2. Logic Solving: Backtracking Search (CSP)

### Why Backtracking?
Sudoku is an NP-complete problem. There is no simple formula to calculate the number in cell X. We must search.

| Algorithm | Suitability | Reasoning |
| :--- | :--- | :--- |
| **Brute Force** | Impossible | $9^{81}$ is too large to search. |
| **Local Search** | Low | Stochastic (Hill Climbing) can get stuck in local optima easily. |
| **Genetic Algorithms** | Medium | Can work, but convergence is slow and inexact. |
| **Backtracking (DFS)** | **High** | Systematically explores assignments. Combined with pruning, it is extremely fast. |

### Heuristics Implemented
To make Backtracking viable for "Hard" puzzles, we implemented:

1.  **MRV (Minimum Remaining Values)**:
    *   *Idea*: "Fail First". Pick the cell with the fewest legal moves (e.g., only 1 or 2 options).
    *   *Effect*: Drastically reduces the branching factor early in the tree.

2.  **Constraint Propagation (Implicit)**:
    *   *Idea*: Forward checking legal moves before assignment.
    *   *Effect*: We never descend a branch that violates rules immediately.
