from environments.games import TicTacToeState
from environments.sudoku import SudokuCSP
from agents.minimax_agent import T3MinimaxAgent
from algorithms.csp_solver import CSPSolver
import time

def play_tictactoe():
    print("\n--- MODE: TIC TAC TOE (Minimax Agent) ---")
    print("You are 'O' (-1). The AI is 'X' (+1).")
    print("AI goes first (Maximizing player).\n")
    
    game = TicTacToeState()
    # Use the high-level Agent class
    ai_agent = T3MinimaxAgent(name="MasterBot", depth=9)
    
    while not game.is_terminal():
        print(f"\nCurrent Board:\n{game}")
        
        if game.get_turn() == 1:
            # AI Turn
            print(f"\n{ai_agent.name} is thinking...")
            start_time = time.time()
            
            # Polymorphic call - we just ask for an action
            move = ai_agent.get_action(game)
            
            end_time = time.time()
            
            # We can still get stats if we want
            stats = ai_agent.get_stats()
            
            print(f"AI chooses position {move}")
            print(f"Nodes evaluated: {stats['nodes_evaluated']}")
            print(f"Time taken: {end_time - start_time:.4f}s")
            game = game.make_move(move)
            
        else:
            # Human Turn
            moves = game.get_legal_moves()
            print(f"\nYour turn! Legal moves: {moves}")
            while True:
                try:
                    choice = int(input("Enter move index (0-8): "))
                    if choice in moves:
                        game = game.make_move(choice)
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a number.")
                    
    print(f"\nFINAL BOARD:\n{game}")
    winner = game.get_winner()
    if winner == 1:
        print("\nAI WINS! (As expected, it is invincible)")
    elif winner == -1:
        print("\nYOU WIN! (This should be impossible)")
    else:
        print("\nDRAW! Perfect game.")

def solve_sudoku():
    print("\n--- MODE: SUDOKU SOLVER (CSP Backtracking) ---")
    # Hardest sudoku example
    hard_puzzle = "8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4.."
    
    print("\nInitial Puzzle:")
    puzzle = SudokuCSP(hard_puzzle)
    print(puzzle)
    
    solver = CSPSolver()
    print("Solving...")
    
    start_time = time.time()
    solved = solver.solve(puzzle)
    end_time = time.time()
    
    if solved:
        print("\nSolved Puzzle:")
        print(puzzle)
        print(f"Nodes visited: {solver.nodes_visited}")
        print(f"Time taken: {end_time - start_time:.4f}s")
    else:
        print("Failed to solve.")

if __name__ == "__main__":
    print("========================================")
    print("  CLASSICAL AI REASONING SYSTEM")
    print("========================================")
    print("1. Play Tic-Tac-Toe (Adversarial Search)")
    print("2. Solve Sudoku (Constraint Satisfaction)")
    
    choice = input("\nSelect mode (1/2): ")
    
    if choice == "1":
        play_tictactoe()
    elif choice == "2":
        solve_sudoku()
    else:
        print("Invalid choice.")
