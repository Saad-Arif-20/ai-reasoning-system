from typing import Tuple, Optional, Any
from environments.games import GameState
import math

class MinimaxAgent:
    """
    An agent that uses Minimax with Alpha-Beta pruning to make optimal moves.
    """
    
    def __init__(self, depth: int = 10):
        self.max_depth = depth
        self.nodes_evaluated = 0

    def get_best_move(self, state: GameState) -> Tuple[Any, float]:
        """
        Returns the best move and its expected value.
        """
        self.nodes_evaluated = 0
        best_val = -math.inf if state.get_turn() == 1 else math.inf
        best_move = None
        
        alpha = -math.inf
        beta = math.inf
        
        # Sort moves for better pruning (heuristic: center > corners > edges for TicTacToe)
        # This is a general framework, but specific sorting helps
        moves = state.get_legal_moves()
        
        for move in moves:
            next_state = state.make_move(move)
            val = self._minimax(next_state, self.max_depth - 1, alpha, beta, False)
            
            # Maximizing player (1)
            if state.get_turn() == 1:
                if val > best_val:
                    best_val = val
                    best_move = move
                alpha = max(alpha, best_val)
                
            # Minimizing player (-1)
            else:
                if val < best_val:
                    best_val = val
                    best_move = move
                beta = min(beta, best_val)
                
            if beta <= alpha:
                break
                
        return best_move, best_val

    def _minimax(self, state: GameState, depth: int, alpha: float, beta: float, maximizing: bool) -> float:
        self.nodes_evaluated += 1
        
        if depth == 0 or state.is_terminal():
            return self._evaluate(state)
        
        # Maximizing player is Player 1 ('X') (controlled by logic, not the 'maximizing' flag,
        # but standard minimax usually assumes recursive calls toggle. 
        # Here we rely on state.get_turn() to know who is playing.)
        
        current_turn = state.get_turn()
        
        if current_turn == 1: # Maximizer
            max_eval = -math.inf
            for move in state.get_legal_moves():
                next_state = state.make_move(move)
                eval_val = self._minimax(next_state, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval_val)
                alpha = max(alpha, eval_val)
                if beta <= alpha:
                    break
            return max_eval
            
        else: # Minimizer
            min_eval = math.inf
            for move in state.get_legal_moves():
                next_state = state.make_move(move)
                eval_val = self._minimax(next_state, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval_val)
                beta = min(beta, eval_val)
                if beta <= alpha:
                    break
            return min_eval

    def _evaluate(self, state: GameState) -> float:
        """
        Heuristic evaluation function.
        In simple games like TicTacToe, we can just return +10 for win, -10 for loss.
        """
        winner = state.get_winner()
        if winner == 1:
            return 10.0
        elif winner == -1:
            return -10.0
        else:
            return 0.0
