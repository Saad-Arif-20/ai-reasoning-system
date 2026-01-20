from typing import List, Tuple, Optional, Set

class SudokuCSP:
    """
    Represents a Sudoku puzzle as a Constraint Satisfaction Problem.
    """
    def __init__(self, board_str: str):
        # Flattened list 0-80
        # board_str is "53..7....6..195..." (0 or . for empty)
        self.board = []
        for char in board_str:
            if char.isdigit() and char != '0':
                self.board.append(int(char))
            else:
                self.board.append(0)
                
    def is_complete(self) -> bool:
        return 0 not in self.board
        
    def get_variables(self) -> List[int]:
        """Return indices of empty cells (variables)."""
        return [i for i, val in enumerate(self.board) if val == 0]
        
    def get_domain(self, var_index: int) -> Set[int]:
        """Return valid values (1-9) for a given cell based on constraints."""
        row = var_index // 9
        col = var_index % 9
        block_row = (row // 3) * 3
        block_col = (col // 3) * 3
        
        used = set()
        
        # Row check
        for c in range(9):
            val = self.board[row * 9 + c]
            if val != 0: used.add(val)
            
        # Column check
        for r in range(9):
            val = self.board[r * 9 + col]
            if val != 0: used.add(val)
            
        # 3x3 Block check
        for r in range(3):
            for c in range(3):
                val = self.board[(block_row + r) * 9 + (block_col + c)]
                if val != 0: used.add(val)
                
        return set(range(1, 10)) - used
        
    def assignment_is_consistent(self, var: int, value: int) -> bool:
        # Optimistic check (domain check handles logic, but this double checks)
        # For simple Sudoku, get_domain is enough filtering.
        return True
        
    def assign(self, var: int, value: int):
        self.board[var] = value
        
    def unassign(self, var: int):
        self.board[var] = 0
        
    def __str__(self):
        res = ""
        for r in range(9):
            if r % 3 == 0 and r != 0:
                res += "------+-------+------\n"
            for c in range(9):
                if c % 3 == 0 and c != 0:
                    res += "| "
                val = self.board[r*9 + c]
                res += (str(val) if val != 0 else ".") + " "
            res += "\n"
        return res
