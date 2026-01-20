from agents.base import Agent
from algorithms.minimax import MinimaxAgent as MinimaxAlgo
from environments.games import GameState
from typing import Any

class T3MinimaxAgent(Agent):
    """
    An agent specifically designed for Tic-Tac-Toe using Minimax logic.
    """
    
    def __init__(self, name: str = "MinimaxBot", depth: int = 9):
        super().__init__(name)
        # We compose the algorithm inside the agent
        self.algo = MinimaxAlgo(depth=depth)
        
    def get_action(self, state: GameState) -> Any:
        # Delegate the thinking to the algorithm
        move, score = self.algo.get_best_move(state)
        return move
        
    def get_stats(self):
        return {
            "nodes_evaluated": self.algo.nodes_evaluated
        }
