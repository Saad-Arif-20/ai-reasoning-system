from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Any
import copy

class GameState(ABC):
    """Abstract base class for a game state in an adversarial search problem."""
    
    @abstractmethod
    def get_legal_moves(self) -> List[Any]:
        """Return a list of legal moves from the current state."""
        pass
    
    @abstractmethod
    def make_move(self, move: Any) -> 'GameState':
        """Return a new GameState after applying the move."""
        pass
    
    @abstractmethod
    def is_terminal(self) -> bool:
        """Return True if the game is over."""
        pass
    
    @abstractmethod
    def get_winner(self) -> Optional[int]:
        """Return the winner ID (1 or -1) or None if draw/not over."""
        pass
    
    @abstractmethod
    def get_turn(self) -> int:
        """Return the ID of the player whose turn it is (1 or -1)."""
        pass
            
    def __repr__(self):
        return str(self)

class TicTacToeState(GameState):
    def __init__(self, board=None, turn=1):
        # 3x3 board represented as list of 9 integers
        # 0 = empty, 1 = Player X, -1 = Player O
        self.board = board if board else [0] * 9
        self.turn = turn # 1 for X, -1 for O

    def get_legal_moves(self) -> List[int]:
        return [i for i, cell in enumerate(self.board) if cell == 0]

    def make_move(self, move: int) -> 'TicTacToeState':
        if self.board[move] != 0:
            raise ValueError(f"Illegal move at index {move}")
        
        new_board = self.board[:]
        new_board[move] = self.turn
        return TicTacToeState(new_board, -self.turn)

    def is_terminal(self) -> bool:
        return self.get_winner() is not None or 0 not in self.board

    def get_winner(self) -> Optional[int]:
        # Winning combinations
        wins = [
            (0,1,2), (3,4,5), (6,7,8), # rows
            (0,3,6), (1,4,7), (2,5,8), # cols
            (0,4,8), (2,4,6)           # diagonals
        ]
        
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != 0:
                return self.board[a]
        
        return None

    def get_turn(self) -> int:
        return self.turn

    def __str__(self):
        symbols = {0: '.', 1: 'X', -1: 'O'}
        rows = [
            [symbols[self.board[3*r + c]] for c in range(3)]
            for r in range(3)
        ]
        return "\n".join(" ".join(row) for row in rows)
