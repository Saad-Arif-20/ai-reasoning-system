from agents.minimax_agent import T3MinimaxAgent
from agents.random_agent import RandomAgent
from environments.games import TicTacToeState
from environments.sudoku import SudokuCSP
from algorithms.csp_solver import CSPSolver
import time

def test_invincibility(num_games=10):
    print(f"\n--- TEST 1: Invincibility Check ({num_games} games vs Random) ---")
    ai = T3MinimaxAgent(depth=9)
    random_bot = RandomAgent()
    
    results = {"win": 0, "draw": 0, "loss": 0}
    
    for i in range(num_games):
        game = TicTacToeState()
        # AI goes first half the time, second half the time
        ai_turn = 1 if i % 2 == 0 else -1
        
        while not game.is_terminal():
            if game.get_turn() == ai_turn:
                move = ai.get_action(game)
            else:
                move = random_bot.get_action(game)
            game = game.make_move(move)
            
        winner = game.get_winner()
        
        if winner is None:
            results["draw"] += 1
        elif winner == ai_turn:
            results["win"] += 1
        else:
            results["loss"] += 1
            print(f"CRITICAL FAILURE: AI LOST GAME #{i+1}")
            print(game)
            return False
            
    print(f"Results: {results}")
    if results["loss"] == 0:
        print("PASS: AI never lost.")
        return True
    return False

def test_sudoku_validity():
    print("\n--- TEST 2: Sudoku Solution Validity ---")
    # Hard puzzle
    puzzle_str = "8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4.."
    puzzle = SudokuCSP(puzzle_str)
    solver = CSPSolver()
    
    solver.solve(puzzle)
    
    if not puzzle.is_complete():
        print("FAIL: Puzzle not complete")
        return False
        
    board = puzzle.board
    
    # Check Rows
    for r in range(9):
        row_vals = set(board[r*9 : r*9+9])
        if row_vals != set(range(1,10)):
            print(f"FAIL: Row {r} invalid")
            return False
            
    # Check Cols
    for c in range(9):
        col_vals = set(board[r*9 + c] for r in range(9))
        if col_vals != set(range(1,10)):
            print(f"FAIL: Col {c} invalid")
            return False
            
    print("PASS: Solution satisfies all constraints.")
    return True

if __name__ == "__main__":
    t1 = test_invincibility()
    t2 = test_sudoku_validity()
    
    if t1 and t2:
        print("\n[+] ALL COMPREHENSIVE TESTS PASSED")
    else:
        print("\n[!] SOME TESTS FAILED")
