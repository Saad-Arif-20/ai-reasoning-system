# Problem Formulation

## 1. Adversarial Search: Tic-Tac-Toe

### Problem Definition
Tic-Tac-Toe is a zero-sum, perfect information, deterministic game.

*   **Initial State**: An empty 3x3 grid.
*   **Player(s)**: 
    *   `MAX` (AI Agent, 'X'): Tries to maximize utility (+10).
    *   `MIN` (Opponent, 'O'): Tries to minimize utility (-10).
*   **Actions**: Placing a mark in any empty cell `(row, col)`.
*   **State Space**: $3^9 = 19,683$ theoretical states (reduced significantly by game logic).
*   **Transition Model**: $Result(S, a) \rightarrow S'$ where $S'$ is the board with action $a$ applied.
*   **Terminal Test**: row, column, or diagonal filled with same symbol OR board full.
*   **Utility Function**:
    *   $+10$ if MAX wins.
    *   $-10$ if MIN wins.
    *   $0$ if Draw.

### Complexity
*   **Game Tree Size**: $9! \approx 362,880$ leaf nodes (upper bound).
*   **Branching Factor**: Starts at 9, decreases by 1 each level.

---

## 2. Constraint Satisfaction: Sudoku

### Problem Definition
Sudoku is a logic puzzle defined by variables, domains, and constraints.

*   **Variables ($X$)**: 81 cells on a 9x9 grid ($x_{0}$ to $x_{80}$).
*   **Domains ($D$)**: Each variable $x_i$ can take values from $\{1, 2, ..., 9\}$.
*   **Constraints ($C$)**:
    *   **Row Constraint**: `Alldiff(x_i)` for all $x_i$ in same row.
    *   **Col Constraint**: `Alldiff(x_i)` for all $x_i$ in same col.
    *   **Box Constraint**: `Alldiff(x_i)` for all $x_i$ in same 3x3 block.

### Search Space
*   **Naive Search**: $9^{81}$ possible assignments (astronomically large).
*   **Constraint Graph**: Logic constraints reduce the effective branching factor significantly (often to < 3 choices per cell).
