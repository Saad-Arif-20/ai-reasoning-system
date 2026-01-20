from typing import Optional, List
from environments.sudoku import SudokuCSP

class CSPSolver:
    """
    Solves Constraint Satisfaction Problems using Backtracking search
    with MRV (Minimum Remaining Values) heuristic.
    """
    
    def __init__(self):
        self.nodes_visited = 0
        
    def solve(self, csp: SudokuCSP) -> bool:
        """Modifies the CSP in-place to the solved state. Returns True if solved."""
        self.nodes_visited = 0
        return self._backtrack(csp)
        
    def _backtrack(self, csp: SudokuCSP) -> bool:
        if csp.is_complete():
            return True
            
        self.nodes_visited += 1
        
        # Select unassigned variable (MRV Heuristic: variable with fewest legal moves)
        var = self._select_unassigned_variable(csp)
        
        # Get ordered domain values
        domain = list(csp.get_domain(var))
        # Simple LCV heuristic: try values in order (could optimize further)
        domain.sort() 
        
        for value in domain:
            if csp.assignment_is_consistent(var, value):
                csp.assign(var, value)
                
                if self._backtrack(csp):
                    return True
                    
                # Backtrack
                csp.unassign(var)
                
        return False
        
    def _select_unassigned_variable(self, csp: SudokuCSP) -> int:
        """
        Selects the variable with the Minimum Remaining Values (MRV).
        """
        variables = csp.get_variables()
        best_var = -1
        min_domain_size = 10 # Max domain is 9
        
        for var in variables:
            domain_size = len(csp.get_domain(var))
            if domain_size < min_domain_size:
                min_domain_size = domain_size
                best_var = var
                
        return best_var
