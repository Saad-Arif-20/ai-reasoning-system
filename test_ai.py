from environments.games import TicTacToeState
from algorithms.minimax import MinimaxAgent
from algorithms.csp_solver import CSPSolver
from environments.sudoku import SudokuCSP
import time

def test_minimax_vs_minimax():
    print("Testing Minimax vs Minimax (Should be a Draw)...")
    game = TicTacToeState()
    ai1 = MinimaxAgent(depth=9) # X
    ai2 = MinimaxAgent(depth=9) # O
    
    while not game.is_terminal():
        current_ai = ai1 if game.get_turn() == 1 else ai2
        move, _ = current_ai.get_best_move(game)
        game = game.make_move(move)
        
    print(f"Final Board:\n{game}")
    winner = game.get_winner()
    
    if winner is None:
        print("RESULT: DRAW [PASS]")
    else:
        print(f"RESULT: Winner {winner} [FAIL - Minimax should draw itself]")

def test_easy_sudoku():
    print("\nTesting Easy Sudoku Solver...")
    easy = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
    puzzle = SudokuCSP(easy)
    solver = CSPSolver()
    
    start = time.time()
    result = solver.solve(puzzle)
    end = time.time()
    
    if result and puzzle.is_complete():
        print(f"RESULT: SOLVED in {end-start:.4f}s [PASS]")
    else:
        print("RESULT: FAILED [FAIL]")

if __name__ == "__main__":
    test_minimax_vs_minimax()
    test_easy_sudoku()
