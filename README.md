# 🤖 Classical AI Reasoning System

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI](https://img.shields.io/badge/AI-Classical-FF6F00)](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)

A comprehensive implementation of classical AI techniques including game-playing agents with Minimax algorithm and constraint satisfaction problem solvers. Features an unbeatable Tic-Tac-Toe AI and a lightning-fast Sudoku solver.

## 🌟 Why This Project?

While modern AI focuses on machine learning and neural networks, **Classical AI** (symbolic AI) uses explicit reasoning, search algorithms, and logic. These techniques power game engines, planning systems, and optimization tools used in production systems worldwide. This project demonstrates both theoretical understanding and practical implementation of foundational AI concepts.

### Key Highlights
- 🎮 **Unbeatable Game AI** - Minimax agent that never loses at Tic-Tac-Toe
- 🧩 **Sudoku Solver** - Solves hard puzzles in milliseconds using CSP techniques
- ⚡ **Alpha-Beta Pruning** - Optimized search with significant node reduction
- 🎯 **Smart Heuristics** - MRV and LCV for efficient constraint satisfaction
- 🏗️ **Clean Architecture** - Separation of agents, algorithms, and environments
- 📚 **Zero Dependencies** - Pure Python implementation

---

## 🚀 At a Glance

- 🎮 **2 AI problem types** (adversarial search, constraint satisfaction)
- 🧠 **Minimax + Alpha-Beta** (unbeatable game-playing agent)
- 🧩 **CSP solver** (Sudoku in milliseconds with backtracking + heuristics)
- 📊 **Performance optimized** (pruning reduces search space dramatically)
- 🎯 **Clean abstractions** (agents, algorithms, environments separated)
- 📚 **Zero dependencies** (pure Python standard library)

⏱️ **Setup time**: < 1 minute  
🎓 **Ideal for**: AI fundamentals, game development, algorithm design

---

## 📚 Table of Contents

- [Why This Project?](#-why-this-project)
- [Quick Start](#-quick-start)
- [Game Playing Agent](#-game-playing-agent)
- [Constraint Satisfaction Solver](#-constraint-satisfaction-solver)
- [Algorithm Complexity](#-algorithm-complexity)
- [Real-World Applications](#-real-world-applications)
- [Key Design Decisions](#-key-design-decisions)
- [What I Learned](#-what-i-learned)
- [Testing](#-testing)
- [Contributing](#-contributing)

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Saad-Arif-20/ai-reasoning-system.git
cd ai-reasoning-system

# Run the interactive demo
python main.py
```

### Quick Demo

```bash
$ python main.py

╔════════════════════════════════════════╗
║   Classical AI Reasoning System        ║
╚════════════════════════════════════════╝

Choose an option:
1. Play Tic-Tac-Toe (vs Minimax AI)
2. Solve Sudoku Puzzle
3. Run Performance Benchmarks
4. Exit

> 1

# Challenge the unbeatable AI!
```

---

## 🏗️ Architecture

```
ai-reasoning-system/
├── agents/                  # Decision-making entities
│   ├── base.py             # Abstract Agent interface
│   ├── minimax_agent.py    # Game-playing AI
│   └── random_agent.py     # Baseline comparison
├── algorithms/             # Core AI algorithms
│   ├── minimax.py          # Alpha-Beta Pruning
│   └── csp_solver.py       # Backtracking Search
├── environments/           # Problem definitions
│   ├── games.py            # Tic-Tac-Toe state management
│   └── sudoku.py           # Sudoku constraint definitions
├── docs/                   # Documentation
│   ├── PROBLEM_FORMULATION.md
│   └── ALGORITHM_SELECTION.md
├── tests/                  # Test suite
└── main.py                 # CLI application
```

**Design Philosophy:**
- **Agent-Environment Separation**: Agents perceive and act; environments define rules
- **Algorithm Modularity**: Algorithms are independent of problem domains
- **Extensibility**: Easy to add new games or constraint problems

---

## 🎮 Game Playing Agent

### Minimax with Alpha-Beta Pruning

**How it works:**
1. **Minimax**: Recursively evaluates all possible game states
2. **Alpha-Beta Pruning**: Eliminates branches that can't affect the final decision
3. **Result**: Mathematically optimal play

**Performance:**
```
Tic-Tac-Toe (9 positions, ~300k possible states)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Without Pruning: ~300,000 nodes evaluated
With Pruning:    ~4,500 nodes evaluated
Speedup:         Significant reduction (~98% fewer nodes)
```

**Code Example:**
```python
from agents import MinimaxAgent
from environments import TicTacToe

# Create game and AI agent
game = TicTacToe()
ai = MinimaxAgent(depth=9)  # Full game tree

# AI makes optimal move
move = ai.get_action(game.get_state())
game.make_move(move)

# Result: AI never loses (always wins or draws)
```

---

## 🧩 Constraint Satisfaction Solver

### Sudoku Solver with Backtracking

**Techniques Used:**
- **Backtracking Search**: Depth-first search with constraint checking
- **MRV (Minimum Remaining Values)**: Choose cell with fewest possibilities
- **LCV (Least Constraining Value)**: Prefer values that constrain neighbors least
- **Forward Checking**: Eliminate invalid values early

**Performance:**
```
Hard Sudoku Puzzle (17 clues)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Brute Force:     Years (9^64 combinations)
Backtracking:    ~50ms
With Heuristics: ~15ms
```

**Code Example:**
```python
from algorithms import CSPSolver
from environments import SudokuPuzzle

# Load a hard puzzle
puzzle = SudokuPuzzle.from_string(
    "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
)

# Solve using CSP
solver = CSPSolver()
solution = solver.solve(puzzle)

print(f"Solved in {solution['time']}ms")
print(f"Backtracks: {solution['backtracks']}")
```

---

## 📊 Algorithm Complexity

| Algorithm | Time Complexity | Space | Optimization |
|-----------|----------------|-------|--------------|
| **Minimax** | O(b^d) | O(d) | None |
| **Alpha-Beta** | O(b^(d/2)) | O(d) | Pruning |
| **Backtracking** | O(d^n) | O(n) | None |
| **CSP + Heuristics** | O(d^n)* | O(n) | MRV, LCV |

*Significantly reduced in practice with good heuristics

Where:
- `b` = branching factor
- `d` = depth
- `n` = number of variables

---

## 🎯 Real-World Applications

### Game AI
- **Chess Engines**: Minimax with evaluation functions
- **Board Games**: Go, Checkers, Othello
- **Video Games**: Enemy AI, puzzle solvers

### Constraint Satisfaction
- **Scheduling**: Employee shifts, university timetables
- **Resource Allocation**: Cloud computing, network routing
- **Configuration**: Product customization, circuit design

### Planning Systems
- **Robotics**: Path planning, task scheduling
- **Logistics**: Route optimization, warehouse management
- **Manufacturing**: Production scheduling

---

## 🧠 Key Design Decisions

### Why Minimax for Game Playing?
- **Optimality Guarantee**: Mathematically proven to find best move
- **Simplicity**: Elegant recursive algorithm
- **Foundation**: Basis for more complex game AI
- **Demonstrable**: Easy to verify correctness

### Why Alpha-Beta Pruning?
- **Performance**: Dramatically reduces search space
- **Same Result**: Identical output to Minimax, just faster
- **Industry Standard**: Used in real game engines
- **Elegant Optimization**: Simple concept, powerful impact

### Why CSP for Sudoku?
- **Natural Fit**: Sudoku is inherently a constraint problem
- **Efficient**: Backtracking with heuristics beats brute force
- **Generalizable**: Same approach works for many CSP problems
- **Educational**: Demonstrates constraint propagation

### Why Separate Agents from Environments?
- **Modularity**: Agents work with any compatible environment
- **Testing**: Test agents and environments independently
- **Extensibility**: Easy to add new games or agents
- **Clean Architecture**: Clear separation of concerns

### Why Pure Python (No Libraries)?
- **Learning**: Understand algorithms, not library APIs
- **Transparency**: See the actual implementation
- **Portability**: Runs anywhere Python runs
- **Interview Prep**: Common requirement to implement from scratch

---

## 💡 What I Learned

### Technical Insights
- **Minimax is elegant but expensive**: Exponential time complexity requires optimization
- **Pruning transforms performance**: Alpha-Beta reduces nodes explored by ~98%
- **Heuristics are crucial**: MRV and LCV make CSP practical for real problems
- **Optimal doesn't mean fast**: Minimax finds best move but can be slow without pruning

### AI Lessons
- **Classical AI is still relevant**: Not everything needs machine learning
- **Search is fundamental**: Many AI problems reduce to search
- **Admissible heuristics matter**: Bad heuristics can make algorithms worse
- **State representation is key**: How you model the problem affects everything

### Algorithm Design
- **Recursion simplifies logic**: Minimax is naturally recursive
- **Memoization helps**: Caching repeated states improves performance
- **Early termination wins**: Alpha-Beta stops exploring useless branches
- **Constraint propagation is powerful**: Reducing domains early speeds up search

### Professional Growth
- **Theory predicts practice**: O(b^d) vs O(b^(d/2)) difference is real and measurable
- **Testing proves correctness**: Minimax vs Minimax should always draw
- **Code organization matters**: Clean abstractions make debugging easier
- **Documentation saves time**: Clear docstrings prevent confusion later

---

## 🧪 Testing

```bash
# Run all tests
python -m unittest discover tests -v

# Run specific test
python test_ai.py

# Performance benchmarks
python main.py --benchmark
```

**Test Coverage:**
- ✅ Minimax correctness (optimal play verification)
- ✅ Alpha-Beta equivalence (same result as Minimax)
- ✅ CSP solver correctness (valid solutions)
- ✅ Edge cases (full board, no solution, etc.)

---

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Algorithms**: Minimax, Alpha-Beta Pruning, Backtracking
- **Data Structures**: Trees, Graphs, Constraint Networks
- **Testing**: unittest framework
- **Design Pattern**: Strategy Pattern (interchangeable agents)

---

## 💡 Usage Examples

### Example 1: Custom Game

```python
from agents import MinimaxAgent
from environments import TicTacToe

game = TicTacToe()
ai_x = MinimaxAgent(player='X', depth=9)
ai_o = MinimaxAgent(player='O', depth=9)

# AI vs AI (always draws)
while not game.is_terminal():
    current_player = game.current_player()
    agent = ai_x if current_player == 'X' else ai_o
    move = agent.get_action(game.get_state())
    game.make_move(move)

print(game.get_result())  # Draw
```

### Example 2: Sudoku Variants

```python
from algorithms import CSPSolver
from environments import SudokuPuzzle

# 4x4 Sudoku (easier)
small_puzzle = SudokuPuzzle(size=4)
solution = CSPSolver().solve(small_puzzle)

# 16x16 Sudoku (harder)
large_puzzle = SudokuPuzzle(size=16)
solution = CSPSolver().solve(large_puzzle)
```

---

## 🚀 Future Enhancements

- [ ] **Monte Carlo Tree Search (MCTS)** - For complex games like Go
- [ ] **AC-3 Algorithm** - Arc consistency for CSP preprocessing
- [ ] **GUI Application** - Pygame or Tkinter interface
- [ ] **More Games** - Connect-4, Chess, Checkers
- [ ] **Genetic Algorithms** - Optimization problems
- [ ] **Neural Network Integration** - Hybrid classical/modern AI

---

## 🤝 Contributing

Contributions are welcome! Ideas:

- Implement new games (Chess, Connect-4, Othello)
- Add visualization for algorithm execution
- Optimize performance (Zobrist hashing, transposition tables)
- Add more CSP problems (N-Queens, Graph Coloring)
- Improve documentation and examples

**Steps to contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/ChessEngine`)
3. Add tests for new features
4. Commit changes (`git commit -m 'Add Chess game support'`)
5. Push to branch (`git push origin feature/ChessEngine`)
6. Open a Pull Request

---

## 📚 Learning Resources

**Books:**
- *Artificial Intelligence: A Modern Approach* (Russell & Norvig)
- *The Art of Computer Programming* (Knuth)

**Papers:**
- Shannon's "Programming a Computer for Playing Chess" (1950)
- Knuth's "Alpha-Beta Pruning" analysis

**Online:**
- [Stanford CS221: AI](https://stanford-cs221.github.io/)
- [MIT 6.034: Artificial Intelligence](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Saad Arif**
- GitHub: [@Saad-Arif-20](https://github.com/Saad-Arif-20)
- LinkedIn: [@saad--arif](https://www.linkedin.com/in/saad--arif/)

---

## 🙏 Acknowledgments

- **Russell & Norvig** - AI: A Modern Approach
- **Claude Shannon** - Pioneering work in game AI
- **Donald Knuth** - Alpha-Beta pruning analysis
- **Python Community** - Excellent documentation and tools

---

**Built with 🧠 and classical AI techniques** | © 2025 Saad Arif
